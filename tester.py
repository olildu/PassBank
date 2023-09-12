import customtkinter

root = customtkinter.CTk()
root.geometry("1280x700")

animated_frame = customtkinter.CTkFrame(root, width=780, height=700, corner_radius=0, fg_color="#282D34")
animated_frame.place(x=500, y=0)  # Start the frame outside the window on the right

main_frame = customtkinter.CTkFrame(animated_frame, width=600, height=600, corner_radius=0, fg_color="#282D34")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

frame1 = customtkinter.CTkFrame(main_frame, width=80, height=80, corner_radius=0)
frame1.place(relx=0.5, rely=0.1, anchor="center")

title = customtkinter.CTkLabel(main_frame, text="F", font=customtkinter.CTkFont(family="Roboto", size=18))
title.place(relx=0.5, rely=0.21, anchor="center")

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

email = customtkinter.CTkLabel(email_frame, text="Email or Username", font=customtkinter.CTkFont(family="Roboto", size=18))
email.pack(anchor="w", pady=40, padx=20)

e = customtkinter.CTkLabel(email_frame, text="RANDOMUSERNAME", font=customtkinter.CTkFont(family="Roboto", size=18))
e.place(x=200, y=35)

password = customtkinter.CTkLabel(password_frame, text="Password", font=customtkinter.CTkFont(family="Roboto", size=18))
password.pack(anchor="w", pady=40, padx=20)

website = customtkinter.CTkLabel(website_frame, text="Website", font=customtkinter.CTkFont(family="Roboto", size=18))
website.pack(anchor="w", pady=30, padx=20)

root.mainloop()
