import re
import pyrebase
import customtkinter
import requests
import random
import string
import pwnedpasswords
import concurrent.futures
from PIL import Image, ImageGrab, ImageFilter
from tkinter import PhotoImage, Frame, Label

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
random_password = ""



def is_email_format(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def show_login():
    main_page.place_forget()
    
    login_page.place(relx=0.5, rely=0.5, anchor="center")

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
                go_login_page()
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
            password_main_frame = customtkinter.CTkFrame(master=root, bg_color="#1A1A1A", fg_color="#1A1A1A", width=1000,height=680)
            add_password_main_frame = customtkinter.CTkFrame(master=root, bg_color="#1A1A1A", fg_color="#1A1A1A", width=1000, height=680)
            add_secure_notes_main_frame = customtkinter.CTkFrame(master=root, bg_color="#1A1A1A", fg_color="#1A1A1A", width=1000, height=680)
            generate_password_main_frame = customtkinter.CTkFrame(master=root, bg_color="#1A1A1A", fg_color="#1A1A1A", width=1000, height=680)
            generate_password_main_frame2 = customtkinter.CTkFrame(master=root, bg_color="#1A1A1A", fg_color="#1A1A1A", width=500, height=720)
            check_password_main_frame = customtkinter.CTkFrame(master=root, bg_color="#1A1A1A", fg_color="#1A1A1A", width=1000, height=630)

            left_sidebar = customtkinter.CTkFrame(root, corner_radius=0, width=250)
            left_sidebar.pack(padx=0, pady=0,anchor='w' , fill='y', expand=True)
            left_sidebar.propagate(False)

            categories_frame = customtkinter.CTkFrame(master=left_sidebar, corner_radius=0)
            tools_frame = customtkinter.CTkFrame(master=left_sidebar, corner_radius=0)

            circle_frame = customtkinter.CTkFrame(master=left_sidebar, width=64 ,height=64, corner_radius=50, fg_color="#212121")
            circle_frame.pack(anchor="w")

            circle_frame_image = PhotoImage(file='temp-profile.png')

            circle_frame_image = customtkinter.CTkLabel(master=circle_frame, text="", image=circle_frame_image, fg_color="#212121")
            circle_frame_image.place(relx=0.5, rely=0.5, anchor="center")

            line = Frame(left_sidebar, bg='#4d4d4d', width=1000, height=1)
            line.place(y=90, x=0)

            categories = customtkinter.CTkFrame(master=left_sidebar, fg_color="#212121")
            categories.pack(anchor="w",pady=(10,0))

            catergories_header = customtkinter.CTkLabel(master=categories, text="Catergories", fg_color="#212121",  font=customtkinter.CTkFont(family="Roboto", size=15))
            catergories_header.grid(row=0, column=0,padx=10 , pady=10)

            closed1 = True
            closed2 = True

            def collapse_function_1(event):
                global closed1
                if closed1:
                    categories_frame.pack_forget()
                    down_arrow.configure(image=PhotoImage(file="images/up-arrow.png"))
                    closed1 = False
                else:
                    categories_frame.pack(padx=0, pady=5, anchor='nw', after=categories)
                    down_arrow.configure(image=PhotoImage(file="images/down-arrow.png"))
                    closed1 = True

            def collapse_function_2(event):
                global closed2
                if closed2:
                    tools_frame.pack_forget()
                    up_arrow.configure(image=PhotoImage(file="images/up-arrow.png"))
                    closed2 = False
                else:
                    tools_frame.pack(padx=0, pady=5, anchor='nw', after=tools)
                    up_arrow.configure(image=PhotoImage(file="images/down-arrow.png"))
                    closed2 = True

            down_arrow = customtkinter.CTkLabel(master=categories, text="", image=PhotoImage(file='images/down-arrow.png'), fg_color="#212121", cursor="hand2")
            down_arrow.grid(row=0, column=1,padx=110)
            down_arrow.bind("<Button-1>", collapse_function_1)


            categories_frame.pack(padx=0, pady=5, anchor='nw')



            def open_password(event):
                password_main_frame.place_forget()
                add_password_main_frame.place_forget()
                generate_password_main_frame.place_forget()
                check_password_main_frame.place_forget()
                add_secure_notes_main_frame.place_forget()
                generate_password_main_frame2.place_forget()

                password_main_frame.place(x=240,y=10)

                add_password_frame1 = customtkinter.CTkFrame(password_main_frame, bg_color="#1A1A1A", fg_color="#1A1A1A", width=1000, height=100)
                add_password_frame1.place(relx=0.5, rely=0.1, anchor="center")
                add_password_frame1.propagate(False)

                customtkinter.CTkLabel(master=add_password_frame1, text="Passwords", font=customtkinter.CTkFont(family="Roboto", size=30, weight="bold")).place(x=60,y=10)
                customtkinter.CTkLabel(master=add_password_frame1, text="Title", font=customtkinter.CTkFont(family="Roboto", size=13)).place(x=61,y=55)

                line = Frame(add_password_frame1, bg='#4d4d4d', width=1100, height=1)
                line.place(y=120, x=70)

                add_password = customtkinter.CTkButton(master=add_password_frame1, text="Add a password",font=customtkinter.CTkFont(family="Roboto", size=15), height=40, width=90, corner_radius=50, fg_color="#0C888D", hover_color="#0BA1A2")
                add_password.place(x=800, y=30)
                add_password.bind("<Button-1>", lambda event, password_saved="": open_add_password(password_saved="", event=""))

                add_password_frame2 = customtkinter.CTkScrollableFrame(password_main_frame, bg_color="#1A1A1A", fg_color="#1A1A1A", width=980, height=500)
                add_password_frame2.place(relx=0.5, rely=0.58, anchor="center")

                data = db.child("users").child(f"{auth.current_user['localId']}").child("passwords").get().val()


                animated_frame = customtkinter.CTkFrame(root, width=780, height=700, corner_radius=0, fg_color="#282D34")
                animated_frame.place(x=1400, y=0)
                main_frame = customtkinter.CTkFrame(animated_frame, width=600, height=600, corner_radius=0, fg_color="#282D34")

                def click_outside_frame(event):
                    animated_frame.place_forget()
                    
                def trash(password_delete,event):
                    db.child("users").child(auth.current_user['localId']).child("passwords").child(password_delete).remove()
                    animated_frame.place_forget()
                    import time
                    time.sleep(0.4)
                    open_password(1)
                    

                def create_main_frame(title_text, username, password, website, color):
                    frame1 = customtkinter.CTkFrame(main_frame, width=80, height=80, corner_radius=8, fg_color=color)
                    frame1.place(relx=0.5, rely=0.1, anchor="center")

                    if len(title_text) == 1:
                        customtkinter.CTkLabel(master=frame1, text=a[:1], font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")
                    else:
                        customtkinter.CTkLabel(master=frame1, text=a[:2], font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")

                    title1 = customtkinter.CTkLabel(main_frame, text=title_text, font=customtkinter.CTkFont(family="Roboto", size=18))
                    title1.place(relx=0.5, rely=0.21, anchor="center")

                    details_frame = customtkinter.CTkFrame(main_frame, width=600, height=300, fg_color="#383C43")
                    details_frame.place(relx=0.5, rely=0.6, anchor="center")
                    details_frame.propagate(False)

                    email_frame = customtkinter.CTkFrame(details_frame, width=600, height=100, corner_radius=0, fg_color="#383C43", bg_color="#383C43")
                    email_frame.pack(pady=(10,0))
                    email_frame.propagate(False)

                    password_frame = customtkinter.CTkFrame(details_frame, width=600, height=100, corner_radius=0, fg_color="#383C43", bg_color="#383C43", border_color="#3E4249", border_width=2)
                    password_frame.pack()
                    password_frame.propagate(False)

                    website_frame = customtkinter.CTkFrame(details_frame, width=600, height=100, corner_radius=0, fg_color="#383C43", bg_color="#383C43")
                    website_frame.pack(pady=(0,10))
                    website_frame.propagate(False)

                    email_label = customtkinter.CTkLabel(email_frame, text="Email or Username", font=customtkinter.CTkFont(family="Roboto", size=18))
                    email_label.pack(anchor="w", pady=40, padx=20)

                    email = customtkinter.CTkLabel(email_frame, text=username, font=customtkinter.CTkFont(family="Roboto", size=18))
                    email.place(x=200, y=35)

                    password_label = customtkinter.CTkLabel(password_frame, text="Password", font=customtkinter.CTkFont(family="Roboto", size=18))
                    password_label.pack(anchor="w", pady=40, padx=20)

                    password = customtkinter.CTkLabel(password_frame, text=password, font=customtkinter.CTkFont(family="Roboto", size=18))
                    password.place(x=200, y=35)

                    website_label = customtkinter.CTkLabel(website_frame, text="Website", font=customtkinter.CTkFont(family="Roboto", size=18))
                    website_label.pack(anchor="w", pady=30, padx=20)

                    website = customtkinter.CTkLabel(website_frame, text=website, font=customtkinter.CTkFont(family="Roboto", size=18))
                    website.place(x=200, y=25)

                    trash_frame = customtkinter.CTkFrame(main_frame, width=160, height=80, corner_radius=8, fg_color="#383C43", cursor="hand2")
                    trash_frame.place(relx=0.38, rely=0.86)
                    trash_frame.propagate(False)
                    trash_frame.bind("<Button-1>", lambda e, password_delete=title_text: trash(password_delete,event=e))

                    trash_image = customtkinter.CTkLabel(master=trash_frame, text="",image=PhotoImage(file="images/delete.png"), font=customtkinter.CTkFont(family="Roboto", size=20))
                    trash_image.place(relx=0.41, rely=0.2)
                    trash_image.bind("<Button-1>", lambda e, password_delete=title_text: trash(password_delete,event=e))
                    
                    trash_label = customtkinter.CTkLabel(master=trash_frame, text="Trash", font=customtkinter.CTkFont(family="Roboto", size=15))
                    trash_label.place(relx=0.38, rely=0.55)
                    trash_label.bind("<Button-1>", lambda e, password_delete=title_text: trash(password_delete,event=e))

                    close = customtkinter.CTkLabel(master=animated_frame, text="",image=PhotoImage(file="images/circle.png"),cursor="hand2", font=customtkinter.CTkFont(family="Roboto", size=20))
                    close.place(x=20, y=20)
                    close.bind("<Button-1>", click_outside_frame)

                def animate_frame(x):
                    if x >= 500:
                        animated_frame.place(x=x, y=0)
                        delay = 1  
                        root.after(delay, animate_frame, x - 7) 
                        main_frame.place(relx=0.5, rely=0.5, anchor="center")

                def frame_click(event, title, username, password, website,color):
                    create_main_frame(title, username, password, website, color)
                    animate_frame(1400)

                for service, service_info in data.items():
                    colors = ["#000080", "#4B0082", "#008080", "#990000", "#355E3B", "#636363", "#9370DB", "#C04000", "#8A9A5B"]
                    random_color = random.choice(colors)

                    frame = customtkinter.CTkFrame(master=add_password_frame2, cursor="hand2")
                    frame.pack(fill="x", pady=10, padx=(50,60))
                    frame.configure(height=100)
                    frame.propagate(False)

                    icon_frame = customtkinter.CTkFrame(master=frame, width=70, height=70, fg_color=random_color)
                    icon_frame.pack(pady=10, padx=20, anchor="w")

                    title_label = customtkinter.CTkLabel(master=frame, text=service_info['title'], font=customtkinter.CTkFont(family="Roboto", size=18))
                    title_label.place(x=110, y=20)

                    title_label1 = customtkinter.CTkLabel(master=frame, text=service_info['username'], font=customtkinter.CTkFont(family="Roboto", size=12), text_color="#95979C")
                    title_label1.place(x=113, y=45)

                    frame.bind("<Button-1>", lambda event,color=icon_frame.cget('fg_color'), title=service_info['title'], username=service_info['username'], password=service_info['password'], website=service_info['website']: frame_click(event, title, username, password, website,color ))

                    a = service_info['title']
                    if len(a) == 1:
                        customtkinter.CTkLabel(master=icon_frame, text=a[:1], font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")
                    else:
                        customtkinter.CTkLabel(master=icon_frame, text=a[:2], font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")

            def open_secure_note(event):
                password_main_frame.place_forget()
                add_password_main_frame.place_forget()
                generate_password_main_frame.place_forget()
                check_password_main_frame.place_forget()
                add_secure_notes_main_frame.place_forget()
                generate_password_main_frame2.place_forget()

                password_main_frame.place(x=240,y=10)

                add_password_frame1 = customtkinter.CTkFrame(password_main_frame, bg_color="#1A1A1A", fg_color="#1A1A1A", width=1000, height=100)
                add_password_frame1.place(relx=0.5, rely=0.1, anchor="center")
                add_password_frame1.propagate(False)

                customtkinter.CTkLabel(master=add_password_frame1, text="Secure Notes", font=customtkinter.CTkFont(family="Roboto", size=30, weight="bold")).place(x=60,y=10)
                customtkinter.CTkLabel(master=add_password_frame1, text="Title", font=customtkinter.CTkFont(family="Roboto", size=13)).place(x=61,y=55)

                line = Frame(add_password_frame1, bg='#4d4d4d', width=1100, height=1)
                line.place(y=120, x=70)

                add_password = customtkinter.CTkButton(master=add_password_frame1, text="Add Secure Note",font=customtkinter.CTkFont(family="Roboto", size=15), height=40, width=90, corner_radius=50, fg_color="#0C888D", hover_color="#0BA1A2")
                add_password.place(x=800, y=30)
                add_password.bind("<Button-1>", open_add_secure_note)

                def animate_frame(x):
                    if x >= 500:
                        animated_frame.place(x=x, y=0)
                        delay = 1  
                        root.after(delay, animate_frame, x - 7) 
                        main_frame.place(relx=0.5, rely=0.5, anchor="center")

                def frame_click(event, title_text, secure_note):
                    create_main_frame(title_text, secure_note)
                    animate_frame(1400)

                def click_outside_frame():
                    animated_frame.place_forget()

                def trash(secure_note_delete,event):
                    print(secure_note_delete)
                    db.child("users").child(auth.current_user['localId']).child("secure notes").child(secure_note_delete).remove()
                    animated_frame.place_forget()
                    import time
                    time.sleep(0.4)
                    open_secure_note(1)

                def create_main_frame(title_text, secure_note):            
                    frame1 = customtkinter.CTkFrame(main_frame, width=80, height=80, corner_radius=8)
                    frame1.place(relx=0.5, rely=0.1, anchor="center")

                    if len(title_text) == 1:
                        customtkinter.CTkLabel(master=frame1, text=title_text[:1], font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")
                    else:
                        customtkinter.CTkLabel(master=frame1, text=title_text[:2], font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")

                    title1 = customtkinter.CTkLabel(main_frame, text=title_text, font=customtkinter.CTkFont(family="Roboto", size=18))
                    title1.place(relx=0.5, rely=0.21, anchor="center")
                    details_frame = customtkinter.CTkFrame(main_frame, width=600, fg_color="#383C43")

                    lines = round(len(secure_note)/50) * 53

                    final = lines + 130
                    print(lines)

                    details_frame.configure(height=final)

                    details_frame.place(x=300, y=300, anchor="center")
                    details_frame.propagate(False)

                    email_frame = customtkinter.CTkFrame(details_frame, width=600, height=100, corner_radius=0, fg_color="#383C43", bg_color="#383C43")
                    email_frame.pack(pady=(10,0))
                    email_frame.propagate(False)

                    email = customtkinter.CTkLabel(email_frame, text=secure_note,wraplength=320,justify="left",anchor="w", font=customtkinter.CTkFont(family="Roboto", size=18))
                    email.place(x=180, y=35)

                    secure_label = customtkinter.CTkLabel(email_frame, text="Secure Note", font=customtkinter.CTkFont(family="Roboto", size=18))
                    secure_label.pack(anchor="w", pady=40, padx=20)

                    trash_frame = customtkinter.CTkFrame(main_frame, width=160, height=80, corner_radius=8, fg_color="#383C43", cursor="hand2")
                    trash_frame.place(relx=0.38, rely=0.86)
                    trash_frame.propagate(False)
                    trash_frame.bind("<Button-1>", lambda e, secure_note_delete=title_text: trash(secure_note_delete,event=e))

                    trash_image = customtkinter.CTkLabel(master=trash_frame, text="",image=PhotoImage(file="images/delete.png"), font=customtkinter.CTkFont(family="Roboto", size=20))
                    trash_image.place(relx=0.41, rely=0.2)
                    trash_image.bind("<Button-1>", lambda e, secure_note_delete=title_text: trash(secure_note_delete,event=e))
                    
                    trash_label = customtkinter.CTkLabel(master=trash_frame, text="Trash", font=customtkinter.CTkFont(family="Roboto", size=15))
                    trash_label.place(relx=0.38, rely=0.55)
                    trash_label.bind("<Button-1>", lambda e, secure_note_delete=title_text: trash(secure_note_delete,event=e))

                    def effectively(event):
                        click_outside_frame()
                        details_frame.destroy()

                    close = customtkinter.CTkLabel(master=animated_frame, text="",image=PhotoImage(file="images/circle.png"),cursor="hand2", font=customtkinter.CTkFont(family="Roboto", size=20))
                    close.place(x=20, y=20)
                    close.bind("<Button-1>", effectively)


                animated_frame = customtkinter.CTkFrame(root, width=780, height=700, corner_radius=0, fg_color="#282D34")
                animated_frame.place(x=1400, y=0)
                main_frame = customtkinter.CTkFrame(animated_frame, width=600, height=600, corner_radius=0, fg_color="#282D34")

                add_password_frame2 = customtkinter.CTkScrollableFrame(password_main_frame, bg_color="#1A1A1A", fg_color="#1A1A1A", width=980, height=500)
                add_password_frame2.place(relx=0.5, rely=0.58, anchor="center")

                data = db.child("users").child(f"{auth.current_user['localId']}").child("secure notes").get().val()

                for service, service_info in data.items():
                    frame = customtkinter.CTkFrame(master=add_password_frame2, cursor="hand2")
                    frame.pack(fill="x", pady=10, padx=(50,60))
                    frame.configure(height=100)
                    frame.propagate(False)

                    icon_frame = customtkinter.CTkFrame(master=frame, width=70, height=70, fg_color="#212121")
                    icon_frame.pack(pady=10, padx=10, anchor="w")

                    title_label = customtkinter.CTkLabel(master=frame, text=service_info['title'], font=customtkinter.CTkFont(family="Roboto", size=18))
                    title_label.place(x=90, y=30)

                    frame.bind("<Button-1>", lambda event, title=service_info['title'], secure_note = service_info['secure note']: frame_click(event, title_text=title, secure_note=secure_note ))


                    customtkinter.CTkLabel(master=icon_frame, text="",image=PhotoImage(file="images/notebook.png"), font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")

            def open_add_secure_note(event):
                password_main_frame.place_forget()
                add_password_main_frame.place_forget()
                generate_password_main_frame.place_forget()
                check_password_main_frame.place_forget()
                generate_password_main_frame2.place_forget()
                
                add_secure_notes_main_frame.place(x=240,y=10)
                add_password_frame = customtkinter.CTkFrame(add_secure_notes_main_frame, bg_color="#1A1A1A", fg_color="#1A1A1A", width=500, height=600)
                add_password_frame.place(relx=0.5, rely=0.5, anchor="center")



                frame1 = customtkinter.CTkFrame(master=add_password_frame, width=70, height=70, fg_color="#1A1A1A")
                frame1.pack(pady=(0,20))
                frame1.propagate(False)

                customtkinter.CTkLabel(master=frame1, text="",image=PhotoImage(file="images/notebook.png"), font=customtkinter.CTkFont(family="Roboto", size=20)).place(relx=0.5, rely=0.5, anchor="center")
                

                def save_data(event):
                    title = title_entry.get()
                    secure_note_text = secure_note.get("1.0", "end-1c")
                    uid = auth.current_user['localId']

                    print(secure_note_text)

                    if title == "":
                        customtkinter.CTkLabel(master=add_password_frame, text='⚠ Please enter a title', font=customtkinter.CTkFont(family="Roboto", size=12), text_color="#F95D68").place(x=10, y=145)
                        if len(title) >= 1:
                            warning.pack(padx=10, anchor="w")
                    else:
                        db.child("users").child(f"{uid}").child("secure notes").child(f"{title}").update({"title": title,"secure note": secure_note_text})
                        open_secure_note(1)

                title_entry = customtkinter.CTkEntry(master=add_password_frame, placeholder_text="Title*", font=customtkinter.CTkFont(family="Roboto", size=15), width=480, height=50 )
                title_entry.pack(pady=2)

                warning = customtkinter.CTkLabel(master=add_password_frame, text='*Required', font=customtkinter.CTkFont(family="Roboto", size=12))
                warning.pack(padx=10, anchor="w")
                
                def on_focus_in(event):
                    if secure_note.get("1.0", "end-1c") == "Secure Note":
                        secure_note.delete("1.0", "end-1c")
                        secure_note.configure(text_color = "#D6D6D6")
                        
                def on_focus_out(event):
                    if secure_note.get("1.0", "end-1c") == "":
                        secure_note.insert("1.0", "Secure Note")
                        secure_note.configure(text_color = "#899296")
                        
                secure_note = customtkinter.CTkTextbox(add_password_frame, activate_scrollbars=True, font=customtkinter.CTkFont(family="Roboto", size=15), text_color="#899296", width=480, height=200, border_color="#565B5E", border_width=2)
                secure_note.pack(pady=(50,10))
                secure_note.insert("1.0", "Secure Note")

                secure_note.bind("<FocusIn>", on_focus_in)
                secure_note.bind("<FocusOut>", on_focus_out)
                
                save_button = customtkinter.CTkButton(master=add_password_frame, text="Save",font=customtkinter.CTkFont(family="Roboto", size=15), height=40, width=90, corner_radius=50, fg_color="#0C888D", hover_color="#0BA1A2")
                save_button.pack()
                save_button.bind("<Button-1>", save_data)

            def open_add_password(event, password_saved):
                password_main_frame.place_forget()
                add_password_main_frame.place_forget()
                generate_password_main_frame.place_forget()
                check_password_main_frame.place_forget()
                generate_password_main_frame2.place_forget()
                
                add_password_main_frame.place(x=240,y=10)
                add_password_frame = customtkinter.CTkFrame(add_password_main_frame, bg_color="#1A1A1A", fg_color="#1A1A1A", width=500, height=600)
                add_password_frame.place(relx=0.5, rely=0.5, anchor="center")
                colors = ["#000080", "#4B0082", "#008080", "#990000", "#355E3B", "#636363", "#9370DB", "#C04000", "#8A9A5B"]
                random_color = random.choice(colors)
                frame1 = customtkinter.CTkFrame(master=add_password_frame, width=70, height=70, fg_color=random_color)

                def open_generate_password_new(event):
                    def destroy_image(event):
                        image_button.place_forget()
                        generate_password_frame.place_forget()

                    x, y = root.winfo_rootx(), root.winfo_rooty()
                    w, h = root.winfo_width(), root.winfo_height()
                    screenshot = ImageGrab.grab(bbox=(x, y, x + w, y + h))
                    blurred_screenshot = screenshot.filter(ImageFilter.GaussianBlur(radius=2))
                    blurred_screenshot.save("screenshot.png")

                    button_image = customtkinter.CTkImage(Image.open("screenshot.png"), size=(1280, 700))
                    image_button = customtkinter.CTkLabel(master=root, text="",image=button_image)
                    image_button.place(relx=0.5, rely=0.5, anchor="center")
                    image_button.bind("<Button-1>", destroy_image)
                    


                    generate_password_frame = customtkinter.CTkFrame(root, width=300, height=600, fg_color="#282D34", corner_radius=8)
                    generate_password_frame.place(relx=0.38, rely=0.5, anchor="center")
                    generate_password_frame.place(x=240,y=10)
                    # generate_password_main_frame.propagate(False)




                    def update_string(event):
                        random_password = password.cget("text")
                        password_1.delete(0, "end")
                        password_1.insert(0, random_password)
                        destroy_image(event=1)

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

                    password = customtkinter.CTkLabel(master=middle_body, text='', wraplength=320,justify="left",anchor="w", font=customtkinter.CTkFont(family="Roboto", size=19, weight="bold"))
                    password.place(x=15,y=10)

                    fill_password = customtkinter.CTkButton(master=middle_body, text="Fill Password", width=200, font=customtkinter.CTkFont(family="Roboto", size=19))
                    fill_password.configure(corner_radius=50, height=30)
                    fill_password.place(relx=0.5, rely=0.8, anchor="center")
                    fill_password.bind("<Button-1>", update_string)

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



                    password_main_frame.winfo_toplevel().lift(password_main_frame)

                    slider_event(8)

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
                    uid = auth.current_user['localId']

                    if title == "":
                        customtkinter.CTkLabel(master=add_password_frame, text='⚠ Please enter a title', font=customtkinter.CTkFont(family="Roboto", size=12), text_color="#F95D68").place(x=10, y=145)
                        if len(title) >= 1:
                            warning.pack(padx=10, anchor="w")
                    else:
                        db.child("users").child(f"{uid}").child("passwords").child(f"{title}").update({"title": title,"username": username,"password": password,"website": webiste_url})
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
                password_1.insert(0, password_saved)

                generate_label = customtkinter.CTkLabel(master=add_password_frame, text='Generate Password', font=customtkinter.CTkFont(family="Sans Seriff", size=14), text_color="#40AFAF", cursor="hand2")
                generate_label.pack(anchor="e")
                generate_label.bind("<Button-1>", open_generate_password_new)
                
                website_address_entry = customtkinter.CTkEntry(master=add_password_frame,placeholder_text="Website Address", font=customtkinter.CTkFont(family="Roboto", size=15), width=480, height=50 )
                website_address_entry.pack(pady=50)   

                save_button = customtkinter.CTkButton(master=add_password_frame, text="Save",font=customtkinter.CTkFont(family="Roboto", size=15), height=40, width=90, corner_radius=50, fg_color="#0C888D", hover_color="#0BA1A2")
                save_button.pack()
                save_button.bind("<Button-1>", save_data)

            def open_generate_password(event):
                password_main_frame.place_forget()
                add_password_main_frame.place_forget()
                generate_password_main_frame.place_forget()
                check_password_main_frame.place_forget()
                generate_password_main_frame2.place_forget()
                
                generate_password_main_frame2.place(x=250,y=0)

                def copy(event):
                    root.clipboard_clear()
                    root.clipboard_append(password.cget("text"))
                    copy_label.configure(text="Copied")
                    copy_text_frame.place(x=845, y=100)

                def copy_leave(event):
                    copy_label.configure(text="Copy")
                    copy_text_frame.place_forget()

                def copy_enter(event):
                    copy_text_frame.place(x=845, y=100)


                def generate(event):
                    num_val = slider.get()
                    slider_event(num_val)
                    generate_text_frame.place(x=780, y=100)

                def generate_leave(event):
                    generate_text_frame.place_forget()

                def generate_enter(event):
                    generate_text_frame.place(x=780, y=100)



                def add(event):
                    add_text_frame.place(x=730, y=100)
                    open_add_password(event=1, password_saved=password.cget("text"))



                def add_leave(event):
                    add_text_frame.place_forget()

                def add_enter(event):
                    add_text_frame.place(x=730, y=100)


                title_frame = customtkinter.CTkFrame(generate_password_main_frame2,width=1030,height=80, fg_color="#262626", corner_radius=0)
                title_frame.pack(fill="x")

                customtkinter.CTkLabel(master=title_frame, text='Password Generator', font=customtkinter.CTkFont(family="Roboto", size=30, weight="bold")).place(relx=0.5, rely=0.5, anchor="center")

                generate_frame = customtkinter.CTkFrame(generate_password_main_frame2, width=1030, height=200, fg_color="#151922", corner_radius=0)
                generate_frame.pack()    

                copy_button = customtkinter.CTkLabel(master=generate_frame, text="",cursor="hand2", font=customtkinter.CTkFont(family="Roboto", size=15), image=PhotoImage(file="images/copy2.png"))
                copy_button.place(x=850, y=140)
                copy_button.bind("<Button-1>", copy)
                copy_button.bind("<Leave>", copy_leave)
                copy_button.bind("<Enter>", copy_enter)

                generate_button = customtkinter.CTkLabel(master=generate_frame, text="",cursor="hand2", font=customtkinter.CTkFont(family="Roboto", size=15), image=PhotoImage(file="images/generate.png"))
                generate_button.place(x=795, y=140)
                generate_button.bind("<Button-1>", generate)
                generate_button.bind("<Leave>", generate_leave)
                generate_button.bind("<Enter>", generate_enter)

                add_button = customtkinter.CTkLabel(master=generate_frame, text="",cursor="hand2", font=customtkinter.CTkFont(family="Roboto", size=15), image=PhotoImage(file="images/cross.png"))
                add_button.place(x=740, y=140)
                add_button.bind("<Button-1>", add)
                add_button.bind("<Leave>", add_leave)
                add_button.bind("<Enter>", add_enter)

                password = customtkinter.CTkLabel(master=generate_frame, wraplength=800,justify="left",anchor="w",text='', font=customtkinter.CTkFont(family="Roboto", size=30, weight="bold"))
                
                copy_text_frame = customtkinter.CTkFrame(generate_frame, width=50, height=30, fg_color="#151922",corner_radius=10)
                copy_text_frame.propagate(False)

                copy_text_frame_inner = customtkinter.CTkFrame(copy_text_frame, fg_color="#262626",corner_radius=10)
                copy_text_frame_inner.pack(fill='both', expand=True)

                copy_label = customtkinter.CTkLabel(copy_text_frame_inner, text="Copy")
                copy_label.pack()

                generate_text_frame = customtkinter.CTkFrame(generate_frame, width=70, height=30, fg_color="#151922",corner_radius=10)
                generate_text_frame.propagate(False)

                generate_text_frame_inner = customtkinter.CTkFrame(generate_text_frame, fg_color="#262626",corner_radius=10)
                generate_text_frame_inner.pack(fill='both', expand=True)

                generate_label = customtkinter.CTkLabel(generate_text_frame_inner, text="Generate")
                generate_label.pack()

                add_text_frame = customtkinter.CTkFrame(generate_frame, width=50, height=30, fg_color="#151922",corner_radius=10)
                add_text_frame.propagate(False)

                add_text_frame_inner = customtkinter.CTkFrame(add_text_frame, fg_color="#262626",corner_radius=10)
                add_text_frame_inner.pack(fill='both', expand=True)

                add_label = customtkinter.CTkLabel(add_text_frame_inner, text="Save")
                add_label.pack()

                details_frame = customtkinter.CTkFrame(generate_password_main_frame2, width=1030, height=500, corner_radius=0)
                length_frame = customtkinter.CTkFrame(details_frame, width=1030, height=100, fg_color="#262626", corner_radius=0)
                length_display = customtkinter.CTkLabel(master=length_frame, text='8', font=customtkinter.CTkFont(family="Roboto", size=19))


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

                password.place(x=115, y=40)

                details_frame.pack()    
                details_frame.propagate(False)

                length_frame.pack()

                length_display.place(x=860, y=38)

                slider = customtkinter.CTkSlider(length_frame, from_=8, to=60, width=230, command=slider_event)
                slider.set(8)
                slider.place(x=610, y=42)

                customtkinter.CTkLabel(master=length_frame, text='Length', font=customtkinter.CTkFont(family="Roboto", size=18)).place(x=175, y=40)

                caps_frame = customtkinter.CTkFrame(details_frame, width=1030, height=100, fg_color="#262626", corner_radius=0)
                caps_frame.pack()

                switch_var1 = customtkinter.StringVar(value="on")
                switch1 = customtkinter.CTkSwitch(caps_frame, text="",variable=switch_var1, onvalue="on", offvalue="off",  switch_height=23, switch_width=45)
                switch1.place(x=830, y=40)

                customtkinter.CTkLabel(master=caps_frame, text='Use capital letter (A-Z)', font=customtkinter.CTkFont(family="Roboto", size=18)).place(x=175, y=40)

                digits_frame = customtkinter.CTkFrame(details_frame, width=1030, height=100, fg_color="#262626", corner_radius=0)
                digits_frame.pack()

                switch_var2 = customtkinter.StringVar(value="on")
                switch2 = customtkinter.CTkSwitch(digits_frame, text="",variable=switch_var2, onvalue="on", offvalue="off",  switch_height=23, switch_width=45)
                switch2.place(x=830, y=40)

                customtkinter.CTkLabel(master=digits_frame, text='Use digitis (0-9)', font=customtkinter.CTkFont(family="Roboto", size=18)).place(x=175, y=40)

                symbols_frame = customtkinter.CTkFrame(details_frame, width=1030, height=140, fg_color="#262626", corner_radius=0)
                symbols_frame.pack()

                switch_var3 = customtkinter.StringVar(value="on")
                switch3 = customtkinter.CTkSwitch(symbols_frame, text="",variable=switch_var3, onvalue="on", offvalue="off", switch_height=23, switch_width=45)
                switch3.place(x=830, y=40)

                customtkinter.CTkLabel(master=symbols_frame, text='Use symbols (@!$%&*)', font=customtkinter.CTkFont(family="Roboto", size=18)).place(x=175, y=40)



                slider_event(8)

            def open_check_password(event):
                password_main_frame.place_forget()
                add_password_main_frame.place_forget()
                generate_password_main_frame.place_forget()
                check_password_main_frame.place_forget()
                check_password_main_frame.place(x=240,y=40)
                check_password_main_frame.propagate(False)
                generate_password_main_frame2.place_forget()

                weak_password_count = 0
                same_password = 0
                pwned_passwords = 0

                def is_strong_password(value):
                    if len(value) < 8:
                        return False

                    if not re.search(r'[A-Z]', value):
                        return False

                    if not re.search(r'[a-z]', value):
                        return False

                    if not re.search(r'[0-9]', value):
                        return False

                    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
                        return False

                    return True

                data = db.child("users").child(f"{auth.current_user['localId']}").child("passwords").get().val()
                if data == None:
                    print("balls")
                    frame1 = customtkinter.CTkFrame(check_password_main_frame, width=900, height=180, fg_color="#212121", corner_radius=8, cursor="hand2")
                    frame1.pack(padx=20,pady=(20,10))
                    frame1.propagate(False)

                    shield = PhotoImage(file="images/new.png")
                    shield = customtkinter.CTkLabel(master=frame1, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=shield)
                    shield.place(x=50,y=40)

                    text1 = customtkinter.CTkLabel(master=frame1, text="Weak Passwords", text_color="#F64F64",font=customtkinter.CTkFont(family="Roboto", size=29))
                    text1.place(x=120,y=43)
                    
                    text2 = customtkinter.CTkLabel(master=frame1, text="Makes your accounts easier to brute force attacks", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=15))
                    text2.place(x=123,y=70)
                    
                    text3 = customtkinter.CTkLabel(master=frame1, text="0", text_color="white",font=customtkinter.CTkFont(family="Roboto", size=40, weight="bold"))
                    text3.place(x=70,y=110)

                    text4 = customtkinter.CTkLabel(master=frame1, text="accounts", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=30, weight="bold"))
                    text4.place(x=103,y=118)

                    frame2 = customtkinter.CTkFrame(check_password_main_frame, width=900, height=180, fg_color="#212121", corner_radius=8, cursor="hand2")
                    frame2.pack(padx=20,pady=10)
                    frame2.propagate(False)

                    copy = PhotoImage(file="images/copy.png")
                    copy = customtkinter.CTkLabel(master=frame2, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=copy)
                    copy.place(x=50,y=40)

                    text1 = customtkinter.CTkLabel(master=frame2, text="Reused Passwords", text_color="#F64F64",font=customtkinter.CTkFont(family="Roboto", size=29))
                    text1.place(x=120,y=43)
                    
                    text2 = customtkinter.CTkLabel(master=frame2, text="Used for multiple accounts", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=15))
                    text2.place(x=123,y=70)
                    
                    text3 = customtkinter.CTkLabel(master=frame2, text="0", text_color="white",font=customtkinter.CTkFont(family="Roboto", size=40, weight="bold"))
                    text3.place(x=70,y=110)

                    text4 = customtkinter.CTkLabel(master=frame2, text="accounts", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=30, weight="bold"))
                    text4.place(x=103,y=118)

                    frame3 = customtkinter.CTkFrame(check_password_main_frame, width=900, height=180, fg_color="#212121", corner_radius=8, cursor="hand2")
                    frame3.pack(padx=20,pady=10)
                    frame3.propagate(False)

                    breach = PhotoImage(file="images/breach.png")
                    breach = customtkinter.CTkLabel(master=frame3, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=breach)
                    breach.place(x=50,y=30)

                    text1 = customtkinter.CTkLabel(master=frame3, text="Data Breach Scanner", text_color="#FF7E23",font=customtkinter.CTkFont(family="Roboto", size=29))
                    text1.place(x=120,y=33)
                    
                    text2 = customtkinter.CTkLabel(master=frame3, text="Find out which passwords were exposed", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=15))
                    text2.place(x=123,y=60)
                    
                    pwned = customtkinter.CTkLabel(master=frame3, text="0", text_color="white",font=customtkinter.CTkFont(family="Roboto", size=40, weight="bold"))
                    pwned.place(x=70,y=105)

                    text4 = customtkinter.CTkLabel(master=frame3, text="accounts", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=30, weight="bold"))
                    text4.place(x=103,y=113)
                    
                    return


                passwords = [value['password'] for value in data.values()]
                passwords.sort()

                for password in passwords:
                    if is_strong_password(password):
                        pass
                    else:
                        weak_password_count += 1

                for x in range(len(passwords)):
                    a = passwords[x]
                    try:
                        b = passwords[x+1]
                    except:
                        break

                    if a == b:
                        same_password += 1

                

                
                frame1 = customtkinter.CTkFrame(check_password_main_frame, width=900, height=180, fg_color="#212121", corner_radius=8, cursor="hand2")
                frame1.pack(padx=20,pady=(20,10))
                frame1.propagate(False)

                shield = PhotoImage(file="images/new.png")
                shield = customtkinter.CTkLabel(master=frame1, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=shield)
                shield.place(x=50,y=40)

                text1 = customtkinter.CTkLabel(master=frame1, text="Weak Passwords", text_color="#F64F64",font=customtkinter.CTkFont(family="Roboto", size=29))
                text1.place(x=120,y=43)
                
                text2 = customtkinter.CTkLabel(master=frame1, text="Makes your accounts easier to brute force attacks", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=15))
                text2.place(x=123,y=70)
                
                text3 = customtkinter.CTkLabel(master=frame1, text=weak_password_count, text_color="white",font=customtkinter.CTkFont(family="Roboto", size=40, weight="bold"))
                text3.place(x=70,y=110)

                text4 = customtkinter.CTkLabel(master=frame1, text="accounts", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=30, weight="bold"))
                text4.place(x=103,y=118)

                frame2 = customtkinter.CTkFrame(check_password_main_frame, width=900, height=180, fg_color="#212121", corner_radius=8, cursor="hand2")
                frame2.pack(padx=20,pady=10)
                frame2.propagate(False)

                copy = PhotoImage(file="images/copy.png")
                copy = customtkinter.CTkLabel(master=frame2, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=copy)
                copy.place(x=50,y=40)

                text1 = customtkinter.CTkLabel(master=frame2, text="Reused Passwords", text_color="#F64F64",font=customtkinter.CTkFont(family="Roboto", size=29))
                text1.place(x=120,y=43)
                
                text2 = customtkinter.CTkLabel(master=frame2, text="Used for multiple accounts", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=15))
                text2.place(x=123,y=70)
                
                text3 = customtkinter.CTkLabel(master=frame2, text=same_password*2, text_color="white",font=customtkinter.CTkFont(family="Roboto", size=40, weight="bold"))
                text3.place(x=70,y=110)

                text4 = customtkinter.CTkLabel(master=frame2, text="accounts", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=30, weight="bold"))
                text4.place(x=103,y=118)

                frame3 = customtkinter.CTkFrame(check_password_main_frame, width=900, height=180, fg_color="#212121", corner_radius=8, cursor="hand2")
                frame3.pack(padx=20,pady=10)
                frame3.propagate(False)

                breach = PhotoImage(file="images/breach.png")
                breach = customtkinter.CTkLabel(master=frame3, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=breach)
                breach.place(x=50,y=30)

                text1 = customtkinter.CTkLabel(master=frame3, text="Data Breach Scanner", text_color="#FF7E23",font=customtkinter.CTkFont(family="Roboto", size=29))
                text1.place(x=120,y=33)
                
                text2 = customtkinter.CTkLabel(master=frame3, text="Find out which passwords were exposed", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=15))
                text2.place(x=123,y=60)
                
                pwned = customtkinter.CTkLabel(master=frame3, text="0", text_color="white",font=customtkinter.CTkFont(family="Roboto", size=40, weight="bold"))
                pwned.place(x=70,y=105)

                text4 = customtkinter.CTkLabel(master=frame3, text="accounts", text_color="#95979C",font=customtkinter.CTkFont(family="Roboto", size=30, weight="bold"))
                text4.place(x=103,y=113)

                def check_password(password):
                    if pwnedpasswords.check(password):
                        return 1
                    else:
                        return 0

                with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                    results = executor.map(check_password, passwords)
                for result in results:
                    pwned_passwords += result
                pwned.configure(text=pwned_passwords)


            passwords_frame = customtkinter.CTkFrame(master=categories_frame, corner_radius=0, cursor="hand2", bg_color="#212121", fg_color="#212121")
            passwords_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
            passwords_frame.bind("<Button-1>", open_password)

            passwords_image = PhotoImage(file="images/password.png")

            passwords_text = customtkinter.CTkLabel(master=passwords_frame, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=passwords_image)
            passwords_text.grid(padx=(10, 3), pady=(0,2), sticky="w", column=0, row=0, ipadx=0)

            passwords_label = customtkinter.CTkLabel(master=passwords_frame, text='Passwords', font=customtkinter.CTkFont(family="Roboto", size=15))
            passwords_label.grid(padx=10, pady=(0,2), sticky="w", column=1, row=0, ipadx=0)
            passwords_label.bind("<Button-1>", open_password)


            secure_note_frame = customtkinter.CTkFrame(master=categories_frame, corner_radius=0, cursor="hand2", bg_color="#212121", fg_color="#212121")
            secure_note_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
            # secure_note_frame.bind("<Button-1>", open_secure_noteword)


            secure_note_image = PhotoImage(file="images/note.png")

            secure_note_text = customtkinter.CTkLabel(master=secure_note_frame, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=secure_note_image)
            secure_note_text.grid(padx=(10, 3), pady=7, sticky="w", column=0, row=0, ipadx=0)

            secure_note_label = customtkinter.CTkLabel(master=secure_note_frame, text='Secure Notes', font=customtkinter.CTkFont(family="Roboto", size=15))
            secure_note_label.grid(padx=10, pady=7, sticky="w", column=1, row=0, ipadx=0)
            secure_note_label.bind("<Button-1>", open_secure_note)

            generate_pass_frame = customtkinter.CTkFrame(master=tools_frame, corner_radius=0, cursor="hand2", bg_color="#212121", fg_color="#212121")
            generate_pass_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
            generate_pass_frame.bind("<Button-1>", open_generate_password)

            generate_pass_image = PhotoImage(file="images/generate_password.png")

            generate_pass_text = customtkinter.CTkLabel(master=generate_pass_frame, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=generate_pass_image)
            generate_pass_text.grid(padx=(10, 3), pady=7, sticky="w", column=0, row=0, ipadx=0)
            generate_pass_text.bind("<Button-1>", open_generate_password)

            generate_pass_label = customtkinter.CTkLabel(master=generate_pass_frame, text='Generate a password', font=customtkinter.CTkFont(family="Roboto", size=15))
            generate_pass_label.grid(padx=10, pady=7, sticky="w", column=1, row=0, ipadx=0)
            generate_pass_label.bind("<Button-1>", open_generate_password)

            check_pass_frame = customtkinter.CTkFrame(master=tools_frame, corner_radius=0, cursor="hand2", bg_color="#212121", fg_color="#212121")
            check_pass_frame.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")
            check_pass_frame.bind("<Button-1>", open_check_password)

            check_pass_image = PhotoImage(file='images/heart.png')

            check_pass_text = customtkinter.CTkLabel(master=check_pass_frame, text="", font=customtkinter.CTkFont(family="Roboto", size=15), image=check_pass_image)
            check_pass_text.grid(padx=(10, 3), pady=7, sticky="w", column=0, row=0, ipadx=0)
            check_pass_text.bind("<Button-1>", open_check_password)

            check_pass_label = customtkinter.CTkLabel(master=check_pass_frame, text='Check password health', font=customtkinter.CTkFont(family="Roboto", size=15))
            check_pass_label.grid(padx=10, pady=7, sticky="w", column=1, row=0, ipadx=0)
            check_pass_label.bind("<Button-1>", open_check_password)



            line = Frame(left_sidebar, bg='#4d4d4d', width=1000, height=1)
            line.pack()

            tools = customtkinter.CTkFrame(master=left_sidebar, fg_color="#212121")
            tools.pack(anchor="w",pady=(5,0))

            tools_header = customtkinter.CTkLabel(master=tools, text="Tools", fg_color="#212121",  font=customtkinter.CTkFont(family="Roboto", size=15))
            tools_header.grid(row=0, column=0,padx=10 , pady=5)

            up_arrow = customtkinter.CTkLabel(master=tools, text="", image=PhotoImage(file='images/down-arrow.png'), fg_color="#212121", cursor="hand2")
            up_arrow.grid(row=0, column=1,padx=150)
            up_arrow.bind("<Button-1>", collapse_function_2)

            tools_frame.pack(padx=0, pady=5, anchor='nw')



            line = Frame(left_sidebar, bg='#4d4d4d', width=1000, height=1)
            line.pack()

            # response = requests.get(auth.get_account_info(id_token=user['idToken'])['users'][0]['photoUrl'])
            # with open("temp-profile.png", "wb") as f:
            #     f.write(response.content)

            my_image = customtkinter.CTkImage(light_image=Image.open("temp-profile.png"),dark_image=Image.open("temp-profile.png"),size=(64, 64))
            profile_picture = PhotoImage(file="temp-profile.png")
            circle_frame = customtkinter.CTkFrame(master=left_sidebar, width=64 ,height=64, corner_radius=50, fg_color="#212121")
            circle_frame.pack(anchor="w")

            circle_frame_image = PhotoImage(file='profile.png')

            circle_frame_image = customtkinter.CTkLabel(master=circle_frame, text="", image=circle_frame_image, fg_color="#212121")
            circle_frame_image.place(relx=0.5, rely=0.5, anchor="center")

            root.geometry("1280x700")
        except requests.exceptions.HTTPError as e:
            if "INVALID_PASSWORD" in str(e):
                password_alerts_login.place(x=22, y=263)
            if "EMAIL_NOT_FOUND" in str(e):
                email_alerts_login.place(x=22, y=186)




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
root.geometry("400x480")
# root.geometry("1280x700")
root.title("PassBank Password Manager")
root.resizable(False, False)

# ------------------------------------------------------------------------------------------------ Main Page ------------------------------------------------------------------------------------------------

main_page = customtkinter.CTkFrame(root)

image = PhotoImage(file="images/Logo.png")
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

main_page.pack(padx=20, pady=20)

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



root.mainloop()