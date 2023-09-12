import re
import pyrebase
import customtkinter
import requests
import random
import string
import time
from PIL import Image
from tkinter import PhotoImage, Frame


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
user = ""

user = auth.sign_in_with_email_and_password("ebinsanthosh@outlook.com", "password")

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
                create_user_var = auth.create_user_with_email_and_password(email, password)
                auth.send_email_verification(create_user_var['idToken'])
        else:
            email_alerts.place(x=22, y=186)



def login():
    email = email_entry.get()
    password = password_entry.get()
    if email == "" or password == "":
        pass
    else:
        try:
            global user
            user = auth.sign_in_with_email_and_password(email, password)
            password_alerts_login.place_forget()
            email_alerts_login.place_forget()
            login_page.place_forget()
            main_page.place_forget()
            main_page.pack_forget()
            response = requests.get(auth.get_account_info(id_token=user['idToken'])['users'][0]['photoUrl'])
            # with open("temp-profile.png", "wb") as f:
                # f.write(response.content)
            my_image = customtkinter.CTkImage(light_image=Image.open("temp-profile.png"),dark_image=Image.open("result.png"),size=(100, 100))
            profile_picture = PhotoImage(file="temp-profile.png")
            image_label = customtkinter.CTkLabel(master=circle_frame, text="",image=my_image, corner_radius=50)
            image_label.place(relx=0.5, rely=0.5, anchor="center")
            left_sidebar.pack(padx=0, pady=0, anchor='nw', fill='y', expand=True)
            root.geometry("1280x700")
        except requests.exceptions.HTTPError as e:
            if "INVALID_PASSWORD" in str(e):
                password_alerts_login.place(x=22, y=263)
            if "EMAIL_NOT_FOUND" in str(e):
                email_alerts_login.place(x=22, y=186)


def show_login():
    main_page.place_forget()
    
    login_page.place(relx=0.5, rely=0.5, anchor="center")


def show_create_user():
    main_page.pack_forget()
    login_page.place_forget()
    create_user_page.place(relx=0.5, rely=0.5, anchor="center")


def go_to_login_page(event):
    create_user_page.place_forget()
    main_page.pack_forget()

    login_page.place(relx=0.5, rely=0.5, anchor="center")


def go_to_create_user_page(event):
    main_page.place_forget()
    login_page.place_forget()
    create_user_page.place(relx=0.5, rely=0.5, anchor="center")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
# root.geometry("400x480")
root.geometry("1280x700")
root.title("")
root.resizable(False, False)

# ------------------------------------------------------------------------------------------------ Main Page ------------------------------------------------------------------------------------------------

main_page = customtkinter.CTkFrame(root)



image = PhotoImage(file="logo.png")
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

# main_page.pack(padx=20, pady=20)

# ------------------------------------------------------------------------------------- Login User ------------------------------------------------------------------------------------------------

login_page = customtkinter.CTkFrame(root)

dashboard_label_1 = customtkinter.CTkLabel(login_page, text="Login", font=customtkinter.CTkFont(family="Rem", size=25))
dashboard_label_1.pack(pady=50, padx=20)

email_entry = customtkinter.CTkEntry(login_page, placeholder_text='Email Address', width=280, height=46)
email_entry.pack(pady=10, padx=20)
email_alerts_login = customtkinter.CTkLabel(login_page, text="Email ID is not registered",
                                      font=customtkinter.CTkFont(family="Roboto", size=13), text_color="#d42f2f")

password_entry = customtkinter.CTkEntry(login_page, placeholder_text='Password', width=280, height=46, show="●")
password_entry.pack(pady=20, padx=20)
password_alerts_login = customtkinter.CTkLabel(login_page, text="Wrong Password",
                                         font=customtkinter.CTkFont(family="Roboto", size=13), text_color="#d42f2f")

login_button_1 = customtkinter.CTkButton(login_page, text="Login", font=customtkinter.CTkFont(family="Roboto", size=20),
                                       corner_radius=50, height=46, width=280,command=login)
login_button_1.pack(pady=10, padx=20)

go_create_user_page = customtkinter.CTkLabel(login_page, text="Not Registered?", font=customtkinter.CTkFont(family="Rem", size=15),
                                       text_color="#306896", cursor="hand2")
go_create_user_page.pack(pady=10, padx=10)
go_create_user_page.bind("<Button-1>", go_to_create_user_page)


# ------------------------------------------------------------------------------------- Create User ------------------------------------------------------------------------------------------------


create_user_page = customtkinter.CTkFrame(root)

dashboard_label = customtkinter.CTkLabel(create_user_page, text="Create Account",
                                         font=customtkinter.CTkFont(family="Rem", size=25), cursor="hand2")
dashboard_label.pack(pady=50, padx=20)

email_entry_create = customtkinter.CTkEntry(create_user_page, placeholder_text='Email Address', width=280, height=46)
email_entry_create.pack(pady=10, padx=20)
email_alerts = customtkinter.CTkLabel(create_user_page, text="Email ID is invalid",
                                      font=customtkinter.CTkFont(family="Roboto", size=13), text_color="#d42f2f")

password_entry_create = customtkinter.CTkEntry(create_user_page, placeholder_text='Password', show="●", width=280,
                                               height=46)
password_entry_create.pack(pady=20, padx=20)
password_alerts = customtkinter.CTkLabel(create_user_page, text="Your password is too short",
                                         font=customtkinter.CTkFont(family="Roboto", size=13), text_color="#d42f2f")

login_button_2 = customtkinter.CTkButton(create_user_page, text="Sign Up",
                                       font=customtkinter.CTkFont(family="Roboto", size=20), corner_radius=50,
                                       height=46, width=280, command=create_user)
login_button_2.pack(pady=10, padx=20)

go_login_page = customtkinter.CTkLabel(create_user_page, text="Already Registered?",
                                       font=customtkinter.CTkFont(family="Rem", size=15), text_color="#306896",
                                       cursor="hand2")
go_login_page.pack(pady=10, padx=10)
go_login_page.bind("<Button-1>", go_to_login_page)

# ------------------------------------------------------------------------------------- Main UI ------------------------------------------------------------------------------------------------

password_main_frame = customtkinter.CTkFrame(master=root, bg_color="#1A1A1A", fg_color="#1A1A1A", width=1000,height=680)
add_password_main_frame = customtkinter.CTkFrame(master=root, bg_color="#1A1A1A", fg_color="#1A1A1A", width=1000, height=680)
generate_password_main_frame = customtkinter.CTkFrame(master=root, bg_color="#1A1A1A", fg_color="#1A1A1A", width=1000, height=680)

left_sidebar = customtkinter.CTkFrame(root, corner_radius=0)
left_sidebar.pack(padx=0, pady=0,anchor='w' , fill='y', expand=True)

app_name = customtkinter.CTkLabel(master=left_sidebar, text='PassBank', font=customtkinter.CTkFont(family="Roboto", size=25))
app_name.pack(padx=20, pady=20, anchor="w")

categories_frame = customtkinter.CTkFrame(master=left_sidebar, corner_radius=0)
categories_frame.pack(padx=0, pady=0, anchor='nw')
    
def open_password(event):
    password_main_frame.place_forget()
    add_password_main_frame.place_forget()
    generate_password_main_frame.place_forget()

    password_main_frame.place(x=240,y=10)



    add_password_frame1 = customtkinter.CTkFrame(password_main_frame, bg_color="#1A1A1A", fg_color="#1A1A1A", width=1000, height=100)
    add_password_frame1.place(relx=0.5, rely=0.1, anchor="center")
    add_password_frame1.propagate(False)

    customtkinter.CTkLabel(master=add_password_frame1, text="Passwords", font=customtkinter.CTkFont(family="Roboto", size=30, weight="bold")).place(x=10,y=10)
    customtkinter.CTkLabel(master=add_password_frame1, text="Title", font=customtkinter.CTkFont(family="Roboto", size=13)).place(x=10,y=55)

    line = Frame(add_password_frame1, bg='#4d4d4d', width=1200, height=1)
    line.place(y=120, x=10)

    add_password = customtkinter.CTkButton(master=add_password_frame1, text="Add a password",font=customtkinter.CTkFont(family="Roboto", size=15), height=40, width=90, corner_radius=50, fg_color="#0C888D", hover_color="#0BA1A2")
    add_password.place(x=800, y=30)
    add_password.bind("<Button-1>", open_add_password)


    add_password_frame2 = customtkinter.CTkFrame(password_main_frame, bg_color="#1A1A1A", fg_color="#1A1A1A", width=980, height=500)
    add_password_frame2.place(relx=0.5, rely=0.58, anchor="center")
    add_password_frame2.propagate(False)

    data = db.child("users").child(f"{auth.current_user['localId']}").get().val()


    for service, service_info in data.items():
        colors = ["#808080", "#000080", "#4B0082", "#008080", "#990000", "#355E3B", "#636363", "#9370DB", "#C04000", "#8A9A5B"]

        random_color = random.choice(colors)

        frame = customtkinter.CTkFrame(master=add_password_frame2, height=80, corner_radius=0)
        frame.pack(fill="x", pady=10)

        icon_frame = customtkinter.CTkFrame(master=frame, width=70, height=70, fg_color=random_color)
        icon_frame.pack(pady=10, padx=20, anchor="w")

        title_label = customtkinter.CTkLabel(master=frame, text=service_info['title'], font=customtkinter.CTkFont(family="Roboto", size=18))
        title_label.place(x=110, y=20)

        title_label1 = customtkinter.CTkLabel(master=frame, text=service_info['username'], font=customtkinter.CTkFont(family="Roboto", size=12), text_color="#95979C")
        title_label1.place(x=113, y=45)

        a = service_info['title']
        if len(a) == 1:
            customtkinter.CTkLabel(master=icon_frame, text=a[:1], font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")
        else:
            customtkinter.CTkLabel(master=icon_frame, text=a[:2], font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")




def open_add_password(event):
    password_main_frame.place_forget()
    generate_password_main_frame.place_forget()
    
    add_password_main_frame.place(x=240,y=10)
    add_password_frame = customtkinter.CTkFrame(add_password_main_frame, bg_color="#1A1A1A", fg_color="#1A1A1A", width=500, height=600)
    add_password_frame.place(relx=0.5, rely=0.5, anchor="center")
    frame1 = customtkinter.CTkFrame(master=add_password_frame, width=70, height=70, fg_color="#2F7398")
    
    def on_entry_change(event):
        a = title_entry.get()
        if len(a) == 1:
            customtkinter.CTkLabel(master=frame1, text=a[:1], font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")
        else:
            customtkinter.CTkLabel(master=frame1, text=a[:2], font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")

    def save_data(event):
        title = title_entry.get()
        username = Email_Username_entry.get()
        password =  password_1.get()
        webiste_url = website_address_entry.get()
        uid = 'GEJguE7TlpPrrAt760a5pdCvZC62'

        if title == "":
            customtkinter.CTkLabel(master=add_password_frame, text='⚠ Please enter a title', font=customtkinter.CTkFont(family="Roboto", size=12), text_color="#F95D68").place(x=10, y=145)
            if len(title) >= 1:
                warning.pack(padx=10, anchor="w")
        else:
            db.child("users").child(f"{uid}").child(f"{title}").update({"title": title,
                                                    "username": username,
                                                    "password": password,
                                                    "webiste": webiste_url})
            open_password(event=1)

    frame1.pack(pady=(0,20))
    frame1.propagate(False)


    title_entry = customtkinter.CTkEntry(master=add_password_frame,placeholder_text="Title*", font=customtkinter.CTkFont(family="Roboto", size=15), width=480, height=50 )
    title_entry.pack(pady=2)
    title_entry.bind("<KeyRelease>", on_entry_change)

    warning = customtkinter.CTkLabel(master=add_password_frame, text='* Required', font=customtkinter.CTkFont(family="Roboto", size=12))
    warning.pack(padx=10, anchor="w")
    
    customtkinter.CTkLabel(master=add_password_frame, text='Login Details', font=customtkinter.CTkFont(family="Roboto", size=19, weight="bold")).pack(pady=(30,5),anchor="w")

    Email_Username_entry = customtkinter.CTkEntry(master=add_password_frame,placeholder_text="Email or Username", font=customtkinter.CTkFont(family="Roboto", size=15), width=480, height=50 )
    Email_Username_entry.pack(pady=8)

    password_1 = customtkinter.CTkEntry(master=add_password_frame,placeholder_text="Password", font=customtkinter.CTkFont(family="Roboto", size=15), width=480, height=50, show="●" )
    password_1.pack()

    generate_label = customtkinter.CTkLabel(master=add_password_frame, text='Generate Password', font=customtkinter.CTkFont(family="Sans Seriff", size=14), text_color="#40AFAF", cursor="hand2")
    generate_label.pack(anchor="e")
    generate_label.bind("<Button-1>", open_generate_password)
    
    website_address_entry = customtkinter.CTkEntry(master=add_password_frame,placeholder_text="Website Address", font=customtkinter.CTkFont(family="Roboto", size=15), width=480, height=50 )
    website_address_entry.pack(pady=50)   

    save_button = customtkinter.CTkButton(master=add_password_frame, text="Save",font=customtkinter.CTkFont(family="Roboto", size=15), height=40, width=90, corner_radius=50, fg_color="#0C888D", hover_color="#0BA1A2")
    save_button.pack()
    save_button.bind("<Button-1>", save_data)

def open_generate_password(event):

    password_main_frame.place_forget()
    add_password_main_frame.place_forget()

    generate_password_main_frame.place(x=240,y=10)
    generate_password_frame = customtkinter.CTkFrame(generate_password_main_frame, width=300, height=600, fg_color="#282D34", corner_radius=8)
    generate_password_frame.place(relx=0.5, rely=0.5, anchor="center")
    generate_pass_frame.propagate(False)

    def slider_event(value):
        caps = switch_var1.get() == "on"
        digits = switch_var2.get() == "on"
        symbols = switch_var3.get() == "on"

        def generate_random_password(length):
            characters = string.ascii_lowercase
            if digits:
                characters += string.digits
            if symbols:
                characters += "@!$%&*"

            if caps:
                characters += string.ascii_uppercase

            if not characters:
                return "Select at least one option"

            password = ''.join(random.choice(characters) for _ in range(length))
            return password

        random_password = generate_random_password(round(value))
        password.configure(text=random_password)
        length_display.configure(text=round(value))



    top_header = customtkinter.CTkFrame(generate_password_frame, height=50, corner_radius=0, fg_color="#282D34")
    top_header.pack(fill="x", padx=5, pady=(5,0))
    top_header.propagate(False)

    customtkinter.CTkLabel(master=top_header, text='Password Generator', font=customtkinter.CTkFont(family="Roboto", size=19, weight="bold")).place(relx=0.5, rely=0.5, anchor="center")


    middle_body = customtkinter.CTkFrame(generate_password_frame, height=160, width=200, corner_radius=0, border_color="#383C43", border_width=1, fg_color="#151922")
    middle_body.pack(fill="x")
    middle_body.propagate(False)
    middle_body.configure(width=350)

    password = customtkinter.CTkLabel(master=middle_body, text='SOMERANDOMPASSWORD', wraplength=320,justify="left",anchor="w", font=customtkinter.CTkFont(family="Roboto", size=19, weight="bold"))
    password.place(x=15,y=10)

    fill_password = customtkinter.CTkButton(master=middle_body, text="Fill Password", width=200, font=customtkinter.CTkFont(family="Roboto", size=19))
    fill_password.configure(corner_radius=50, height=30)
    fill_password.place(relx=0.5, rely=0.8, anchor="center")

    middle_lower_body = customtkinter.CTkFrame(generate_password_frame, height=80, corner_radius=0, fg_color="#282D34",border_color="#383C43", border_width=1)
    middle_lower_body.pack(fill="x")
    middle_lower_body.propagate(False)

    customtkinter.CTkLabel(master=middle_lower_body, text='Length', font=customtkinter.CTkFont(family="Roboto", size=19)).place(x=40,y=25)

    slider = customtkinter.CTkSlider(middle_lower_body, from_=8, to=60, width=130, command=slider_event)
    slider.set(8)
    slider.place(x=130,y=30)

    length_display = customtkinter.CTkLabel(master=middle_lower_body, text='55', font=customtkinter.CTkFont(family="Roboto", size=19))
    length_display.place(x=280,y=25)

    lower_body = customtkinter.CTkFrame(generate_password_frame,height=160, corner_radius=0, fg_color="#282D34",border_color="#383C43", border_width=1)
    lower_body.pack(fill="x", pady=(0,5))
    lower_body.propagate(False)

    customtkinter.CTkLabel(master=lower_body, text='Use Capital Letter (A-Z)', font=customtkinter.CTkFont(family="Roboto", size=15)).place(x=30,y=20)
    switch_var1 = customtkinter.StringVar(value="on")
    switch1 = customtkinter.CTkSwitch(lower_body, text="",variable=switch_var1, onvalue="on", offvalue="off")
    switch1.place(x=260,y=20)

    customtkinter.CTkLabel(master=lower_body, text='Use digits (0-9)', font=customtkinter.CTkFont(family="Roboto", size=15)).place(x=30,y=60)
    switch_var2 = customtkinter.StringVar(value="on")
    switch2 = customtkinter.CTkSwitch(lower_body, text="",variable=switch_var2, onvalue="on", offvalue="off")
    switch2.place(x=260,y=60)

    customtkinter.CTkLabel(master=lower_body, text='Use symbols (@!$%&*)', font=customtkinter.CTkFont(family="Roboto", size=15)).place(x=30,y=100)
    switch_var3 = customtkinter.StringVar(value="on")
    switch3 = customtkinter.CTkSwitch(lower_body, text="",variable=switch_var3, onvalue="on", offvalue="off")
    switch3.place(x=260,y=100)   

    slider_event(8)


passwords_frame = customtkinter.CTkFrame(master=categories_frame, corner_radius=0, cursor="hand2", bg_color="#212121", fg_color="#212121")
passwords_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
passwords_frame.bind("<Button-1>", open_password)

passwords_image = PhotoImage(file="password.png")

passwords_text = customtkinter.CTkLabel(master=passwords_frame, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=passwords_image)
passwords_text.grid(padx=(10, 3), pady=7, sticky="w", column=0, row=0, ipadx=0)

passwords_label = customtkinter.CTkLabel(master=passwords_frame, text='Passwords', font=customtkinter.CTkFont(family="Roboto", size=15))
passwords_label.grid(padx=10, pady=7, sticky="w", column=1, row=0, ipadx=0)
passwords_label.bind("<Button-1>", open_password)


add_pass_frame = customtkinter.CTkFrame(master=categories_frame, corner_radius=0, cursor="hand2", bg_color="#212121", fg_color="#212121")
add_pass_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
add_pass_frame.bind("<Button-1>", open_add_password)


add_pass_image = PhotoImage(file="add_password.png")

add_pass_text = customtkinter.CTkLabel(master=add_pass_frame, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=add_pass_image)
add_pass_text.grid(padx=(10, 3), pady=7, sticky="w", column=0, row=0, ipadx=0)

add_pass_label = customtkinter.CTkLabel(master=add_pass_frame, text='Add a new password', font=customtkinter.CTkFont(family="Roboto", size=15))
add_pass_label.grid(padx=10, pady=7, sticky="w", column=1, row=0, ipadx=0)
add_pass_label.bind("<Button-1>", open_add_password)

generate_pass_frame = customtkinter.CTkFrame(master=categories_frame, corner_radius=0, cursor="hand2", bg_color="#212121", fg_color="#212121")
generate_pass_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
generate_pass_frame.bind("<Button-1>", open_generate_password)


generate_pass_image = PhotoImage(file="generate_password.png")

generate_pass_text = customtkinter.CTkLabel(master=generate_pass_frame, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=generate_pass_image)
generate_pass_text.grid(padx=(10, 3), pady=7, sticky="w", column=0, row=0, ipadx=0)
generate_pass_text.bind("<Button-1>", open_generate_password)

generate_pass_label = customtkinter.CTkLabel(master=generate_pass_frame, text='Generate a password', font=customtkinter.CTkFont(family="Roboto", size=15))
generate_pass_label.grid(padx=10, pady=7, sticky="w", column=1, row=0, ipadx=0)
generate_pass_label.bind("<Button-1>", open_generate_password)

check_pass_frame = customtkinter.CTkFrame(master=categories_frame, corner_radius=0, cursor="hand2", bg_color="#212121", fg_color="#212121")
check_pass_frame.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")

check_pass_image = PhotoImage(file='heart.png')

check_pass_text = customtkinter.CTkLabel(master=check_pass_frame, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=check_pass_image)
check_pass_text.grid(padx=(10, 3), pady=7, sticky="w", column=0, row=0, ipadx=0)

check_pass_label = customtkinter.CTkLabel(master=check_pass_frame, text='Check password Health', font=customtkinter.CTkFont(family="Roboto", size=15))
check_pass_label.grid(padx=10, pady=7, sticky="w", column=1, row=0, ipadx=0)


circle_frame = customtkinter.CTkFrame(master=left_sidebar, width=100 ,height=100, corner_radius=50)
circle_frame.pack(padx=10, pady=10, anchor="w")

root.mainloop()