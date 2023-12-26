import customtkinter as ctk
from randPass import generate_password
from addPass import addPassword
import tkinter as tk
from tkinter import ttk
import sqlite3

def password():
    length = length_scale.get()
    password = generate_password(int(length))
    password_label.configure(text=f"{password} is copied to your clipboard")
    addPassword(webEntry.get(), password)

def slider_callback(value):
    # value = length_scale.get()
    scale_label.configure(text=f"The password length is {int(value)}")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
# # Create the main window
window = ctk.CTk()
window.title("Random Password Generator")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0 ,weight=0)
window.grid_columnconfigure(1 ,weight=1)

# Set the height and width of the window
window.geometry("1200x700")

Leftframe = ctk.CTkFrame(window,width=500,height=500)
Leftframe.grid(row=0, column=0, padx=10, pady=10,sticky="nsew")

Leftframe.grid_rowconfigure(0, weight=1)
Leftframe.grid_columnconfigure((0,1,2), weight=1)

frame= ctk.CTkFrame(Leftframe,fg_color="transparent")
frame.grid(row=0, column=1, padx=10, pady=10,sticky="ew")

webLable = ctk.CTkLabel(frame, text="Enter Website Name:")
webLable.pack(padx=10, pady=10)

webEntry = ctk.CTkEntry(frame,placeholder_text="Enter Website Name",corner_radius=10)
webEntry.pack(padx=10, pady=10)

# Create the widgets
length_label = ctk.CTkLabel(frame, text="Password Length:")
length_label.pack(padx=10, pady=10)


length_scale = ctk.CTkSlider(frame, from_=8, to=20,number_of_steps=12,command=slider_callback)
length_scale.set(12)
length_scale.pack(padx=10, pady=10)

scale_label = ctk.CTkLabel(frame, text="The password length is 12")
scale_label.pack(padx=10, pady=10)

generate_button = ctk.CTkButton(frame, text="Generate Password", command=password)
generate_button.pack(padx=10, pady=10)

password_label = ctk.CTkLabel(frame, text="")
password_label.pack(padx=10, pady=10)

Rightframe = ctk.CTkFrame(window,fg_color="#212121")
Rightframe.grid(row=0, column=1, padx=10, pady=10,sticky="nsew")


import tkinter
from tkinter import ttk
import customtkinter


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

# Fetch all the records from the database
cursor.execute("SELECT * FROM passwords")
records = cursor.fetchall()
# print(records)


frame_1 = customtkinter.CTkFrame(master=Rightframe)
frame_1.pack( fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame_1,text="Password Table")
label.pack(pady=10)

##Treeview Customisation (theme colors are selected)
bg_color = window._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
text_color = window._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
selected_color = window._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])

treestyle = ttk.Style()
treestyle.theme_use('default')
treestyle.configure("Treeview.Heading", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
window.bind("<<TreeviewSelect>>", lambda event: window.focus_set())



##Treeview widget data
treeview = ttk.Treeview(frame_1, column=("ID","Website","Username","Password") ,show='tree')
treeview.pack(padx=10,fill="both", expand=True)
treeview.heading("#1", text="ID")
treeview.heading("#2", text="Website")
treeview.heading("#3", text="Username")
treeview.heading("#4", text="Password")
treeview.column("#0", width=4,minwidth=4)
for record in records:
    id = record[0]
    website = record[1]
    password = record[2]
    username = record[3]
    treeview.insert(parent='', index="end", iid=id,  values=(id,website,username))
    treeview.insert(parent=id, index="end" , values=(password))
    # treeview.move(f"{id}.1", id, "end")

treeview.insert('', 0, values=("ID","Website","Username"))


# Close the database connection
conn.close()




# Start the main loop
window.mainloop()

