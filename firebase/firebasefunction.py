from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Flask route to view users
@app.route('/users')
def view_users():
    users = []  # Placeholder for users
    # Fetch users from Firestore
    users_ref = db.collection('users')
    docs = users_ref.get()
    for doc in docs:
        users.append(doc.to_dict())
    return render_template('users.html', users=users)

# Flask route to remove user
@app.route('/remove_user/<user_id>')
def remove_user(user_id):
    # Delete user from Firestore
    user_ref = db.collection('users').document(user_id)
    user_ref.delete()
    return redirect(url_for('view_users'))

# Flask route to edit user details
@app.route('/edit_user/<user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if request.method == 'POST':
        # Update user details in Firestore
        user_ref = db.collection('users').document(user_id)
        user_ref.update({
            'name': request.form['name'],
            'email': request.form['email']
        })
        return redirect(url_for('view_users'))
    else:
        # Fetch user details from Firestore
        user_ref = db.collection('users').document(user_id)
        user_details = user_ref.get().to_dict()
        return render_template('edit_user.html', user_details=user_details)

# Flask route to add user
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Add user to Firestore
        new_user = {
            'name': request.form['name'],
            'email': request.form['email']
        }
        db.collection('users').add(new_user)
        return redirect(url_for('view_users'))
    else:
        return render_template('add_user.html')

if __name__ == '__main__':
    app.run(debug=True)
