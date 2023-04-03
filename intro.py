import customtkinter

# set appearance
customtkinter.set_appearance_mode("System")
#set color theme
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

#geometry of root element
root.geometry("500x350")

def login():
    print("Test")


#where we're going to put all the stuff
frame = customtkinter.CTkFrame(master=root)
#we can also use fram.grid
frame.pack(pady=20, padx=60, fill="both", expand=True)

#add a label, we're adding it to the frame, not the root
label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

#now add two text entry
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

#for password, we don't wanna have it shown, so we add a symbol with "show"
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

#login button, connect it to the function login with command=
button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

#checkbox.
checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()