import re
import pyrebase
import customtkinter
from tkinter import PhotoImage
import requests

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


def is_email_format(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def create_user():
    email = email_entry_create.get()
    password = password_entry_create.get()
    if email == "" or password == "":
        pass
    else:
        if is_email_format(email):
            email_alerts.place_forget()
            if len(password) <= 7:
                password_alerts.place(x=22, y=263)
            else:
                email_alerts.place_forget()
                password_alerts.place_forget()
                user = auth.create_user_with_email_and_password(email, password)
                auth.send_email_verification(user['idToken'])
        else:
            email_alerts.place(x=22, y=186)

def login():
    email = email_entry.get()
    password = password_entry.get()
    if email == "" or password == "":
        pass
    else:
        try:
            auth.sign_in_with_email_and_password(email, password)
            password_alerts_login.place_forget()
            email_alerts_login.place_forget()
            print("Login successful")
        except requests.exceptions.HTTPError as e:
            if "INVALID_PASSWORD" in str(e):
                print("Wrong Password")
                password_alerts_login.place(x=22, y=263)
            if "EMAIL_NOT_FOUND" in str(e):
                email_alerts_login.place(x=22, y=186)


def show_login():
    main_page.place_forget()
    create_user_page.place_forget()
    login_page.place(relx=0.5, rely=0.5, anchor="center")


def show_create_user():
    main_page.place_forget()
    login_page.place_forget()
    create_user_page.place(relx=0.5, rely=0.5, anchor="center")


def go_to_login_page(event):
    create_user_page.place_forget()
    login_page.place(pady=100, padx=50, relx=0.5, rely=0.5, anchor="center")


def go_to_create_user_page(event):
    main_page.place_forget()
    login_page.place_forget()
    create_user_page.place(pady=100, padx=50, relx=0.5, rely=0.5, anchor="center")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x480")
root.title("")
root.resizable(False, False)

main_page = customtkinter.CTkFrame(root)

image = PhotoImage(file="Logo.png")
Logo = customtkinter.CTkLabel(main_page, text="", height=20, width=20, image=image)
Logo.pack(pady=50, padx=10)

Welcome_Label = customtkinter.CTkLabel(main_page, text="Welcome to PassBank",
                                       font=customtkinter.CTkFont(family="Rem", size=25), corner_radius=50, height=46,
                                       width=260)
Welcome_Label.pack(pady=0, padx=20)

create_account_button = customtkinter.CTkButton(main_page, text="Create Account",
                                                font=customtkinter.CTkFont(family="Roboto", size=15), corner_radius=50,
                                                height=46, width=280, command=show_create_user)
create_account_button.pack(pady=15, padx=20)

login_button = customtkinter.CTkButton(main_page, text="Login", font=customtkinter.CTkFont(family="Roboto", size=15),
                                       corner_radius=50, height=46, width=280, command=show_login)
login_button.pack(pady=10, padx=20)

login_page = customtkinter.CTkFrame(root)

dashboard_label = customtkinter.CTkLabel(login_page, text="Login", font=customtkinter.CTkFont(family="Rem", size=25))
dashboard_label.pack(pady=50, padx=20)

email_entry = customtkinter.CTkEntry(login_page, placeholder_text='Email Address', width=280, height=46)
email_entry.pack(pady=10, padx=20)
email_alerts_login = customtkinter.CTkLabel(login_page, text="Email ID is not registered",
                                      font=customtkinter.CTkFont(family="Roboto", size=13), text_color="#d42f2f")

password_entry = customtkinter.CTkEntry(login_page, placeholder_text='Password', width=280, height=46)
password_entry.pack(pady=20, padx=20)
password_alerts_login = customtkinter.CTkLabel(login_page, text="Wrong Password",
                                         font=customtkinter.CTkFont(family="Roboto", size=13), text_color="#d42f2f")

login_button = customtkinter.CTkButton(login_page, text="Login", font=customtkinter.CTkFont(family="Roboto", size=20),
                                       corner_radius=50, height=46, width=280,command=login)
login_button.pack(pady=10, padx=20)

go_login_page = customtkinter.CTkLabel(login_page, text="Go Back", font=customtkinter.CTkFont(family="Rem", size=15),
                                       text_color="#306896", cursor="hand2")
go_login_page.pack(pady=10, padx=10)
go_login_page.bind("<Button-1>", go_to_create_user_page)

main_page.pack(padx=20, pady=20)

create_user_page = customtkinter.CTkFrame(root)

dashboard_label = customtkinter.CTkLabel(create_user_page, text="Create Account",
                                         font=customtkinter.CTkFont(family="Rem", size=25), cursor="hand2")
dashboard_label.pack(pady=50, padx=20)

email_entry_create = customtkinter.CTkEntry(create_user_page, placeholder_text='Email Address', width=280, height=46)
email_entry_create.pack(pady=10, padx=20)
email_alerts = customtkinter.CTkLabel(create_user_page, text="Email ID is invalid",
                                      font=customtkinter.CTkFont(family="Roboto", size=13), text_color="#d42f2f")

password_entry_create = customtkinter.CTkEntry(create_user_page, placeholder_text='Password', show="*", width=280,
                                               height=46)
password_entry_create.pack(pady=20, padx=20)
password_alerts = customtkinter.CTkLabel(create_user_page, text="Your password is too short",
                                         font=customtkinter.CTkFont(family="Roboto", size=13), text_color="#d42f2f")

login_button = customtkinter.CTkButton(create_user_page, text="Sign Up",
                                       font=customtkinter.CTkFont(family="Roboto", size=20), corner_radius=50,
                                       height=46, width=280, command=create_user)
login_button.pack(pady=10, padx=20)

go_login_page = customtkinter.CTkLabel(create_user_page, text="Go Back",
                                       font=customtkinter.CTkFont(family="Rem", size=15), text_color="#306896",
                                       cursor="hand2")
go_login_page.pack(pady=10, padx=10)
go_login_page.bind("<Button-1>", go_to_login_page)

root.mainloop()
