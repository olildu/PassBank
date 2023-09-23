import pyrebase

# Initialize Firebase
config = {
    "apiKey": "AIzaSyDO9WgyHMwZwu3n5O2kt55AQ8HcRMYZcGc",
    "authDomain": "password-manager-olildu.firebaseapp.com",
    "projectId": "password-manager-olildu",
    "databaseURL": "https://password-manager-olildu-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "storageBucket": "password-manager-olildu.appspot.com",
    "messagingSenderId": "665242184560",
    "appId": "1:665242184560:web:9a2ebda5f21f0cfedffdb5",
    "measurementId": "G-RDXEQS1P07"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Sign in the user
user = auth.sign_in_with_email_and_password("ebinsanthosh@outlook.com", "password")

check = auth.get_account_info(user['idToken'])['users'][0]['emailVerified']

print(check)

if check:
    print("User's email is verified.")
else:
    print("User's email is not verified.")
