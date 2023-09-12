import re
import pyrebase
import customtkinter
from tkinter import PhotoImage

firebaseConfig = {
    "apiKey": "AIzaSyDO9WgyHMwZwu3n5O2kt55AQ8HcRMYZcGc",
    "authDomain": "password-manager-olildu.firebaseapp.com",
    "projectId": "password-manager-olildu",
    "databaseURL": "https://password-manager-olildu-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "storageBucket": "password-manager-olildu.appspot.com",
    "messagingSenderId": "665242184560",
    "appId": "1:665242184560:web:9a2ebda5f21f0cfedffdb5",
    "measurementId": "G-RDXEQS1P07"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("ebinsanthosh@outlook.com", "password")
# auth.update_profile(photo_url="myre.com", id_token=user['idToken'])

import requests

response = requests.post("https://identitytoolkit.googleapis.com/v1/accounts:update?key=AIzaSyDO9WgyHMwZwu3n5O2kt55AQ8HcRMYZcGc", headers={"Content-Type": "application/json"}, json={
    "idToken": user['idToken'],
    "photoUrl": "https://ui-avatars.com/api/?rounded=true&name=Ebin+Santhosh",
})
a = auth.get_account_info(id_token=user['idToken'])['users'][0]['displayName']

uid = auth.current_user['localId']

data = db.child("users").child(f"{uid}").get()
print(data.val())