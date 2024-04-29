'''import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:/Users/abelj/Downloads/flutter-hosmngment-firebase-adminsdk-dj8hb-40853f1068.json")
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()

# Function to retrieve location data for a specific user
def get_user_location(user_id):
    # Reference to the 'coordinates/location' document for the specific user
    doc_ref = db.collection('coordinates').document(user_id)

    # Get the document snapshot
    doc = doc_ref.get()

    # Check if the document exists and contains data for the user
    if doc.exists:
        data = doc.to_dict()
        return data
    else:
        return None

# Example usage
user_id = "OybDXDR2PASjSpPn2ZnC3AV1wst1"  # Replace this with the actual user ID
location_data = get_user_location(user_id)
if location_data:
    location = location_data.get('location')
    print("Latitude:", location.latitude)
    print("Longitude:", location.longitude)
    print("Time:", location_data.get('time'))
    print("Username:", location_data.get('username'))
else:
    print("No location data found for the user.")
'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:/Users/abelj/Downloads/flutter-hosmngment-firebase-adminsdk-dj8hb-40853f1068.json")
firebase_admin.initialize_app(cred)

# Function to get all user details
def get_all_users():
    # List all users
    users = auth.list_users()
    user_list = []
    for user in users.iterate_all():
        user_dict = {
            "uid": user.uid,
            "email": user.email,
            "display_name": user.email.toString().split('@').first,
            "phone_number": user.phone_number,
            "email_verified": user.email_verified,
            "disabled": user.disabled,
            "metadata": {
                "creation_time": user.user_metadata.creation_timestamp,
                "last_sign_in_time": user.user_metadata.last_sign_in_timestamp
            }
        }
        user_list.append(user_dict)
    return user_list

# Example usage
all_users = get_all_users()
for user in all_users:
    print("User ID:", user["uid"])
    print("Email:", user["email"])
    print("Display Name:", user["display_name"])
    print("Phone Number:", user["phone_number"])
    print("Email Verified:", user["email_verified"])
    print("Disabled:", user["disabled"])
    print("Creation Time:", user["metadata"]["creation_time"])
    print("Last Sign-in Time:", user["metadata"]["last_sign_in_time"])
    print("\n")
