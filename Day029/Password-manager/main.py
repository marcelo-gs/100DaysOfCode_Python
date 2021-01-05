import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from random import choice, randint, shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    txt_password.delete(0,tkinter.END)
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symb = [choice(symbols) for _ in range(randint(2, 4))]
    password_numb = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letter + password_symb + password_numb
    shuffle(password_list)
    pyperclip.copy("".join(password_list))
    txt_password.insert(0,"".join(password_list)) 
# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    try:
        with open("data.json", "r") as data_file:
            #Reading old data
            data = json.load(data_file)        
    except FileNotFoundError:
        messagebox.showwarning(title="Something is wrong", message="No Data File Found")
        data = None
        return 
    finally:
        website = txt_web_site.get()
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(title=f"{website} - Password Found", 
                                        message=f"Email: {email}\nPassword: {password}\nPassword copied to your clipboard")
        else:
            messagebox.showwarning(title="Something is wrong", message=f"No details for  {website} exists.")

def save_passord():

    website = txt_web_site.get()
    email = txt_email.get()
    password = txt_password.get()
    message = ""
    if website.strip() == "":
        message = "Website is missing\n"
    if password.strip() == "":
        message += "Password is missing\n"
    if email.strip() == "":
        message += "Email/Username is missing\n"

    if len(message) > 0:
        message = message[:-1]
        messagebox.showwarning(title="Something is wrong", message=message)
        return 
    
    new_data = {
            website :{
                "email": email,
                "password":password
            }
    }
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}\nPassword: {password}\nIs it ok to save?")

    if is_ok:

        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)        
                #Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
            txt_web_site.delete(0,tkinter.END)
            txt_password.delete(0,tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #

#####Create objects
window = tkinter.Tk()

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)

img_lock = tkinter.PhotoImage(file="logo.png")

lbl_webSite = tkinter.Label()
lbl_email = tkinter.Label()
lbl_password = tkinter.Label()

txt_web_site = tkinter.Entry(width=35)
txt_email  = tkinter.Entry(width=35)
txt_password = tkinter.Entry(width=21)

btn_add = tkinter.Button(width=34)
btn_gen_pw = tkinter.Button(width=15)
btn_search = tkinter.Button(width=15)

#####Setup Objects
#Window
window.title("Password Manager")
window.config(padx=20, pady=20)
##window.minsize(width=200, height=200)

#Label
lbl_webSite.config(text="Website:")
lbl_email.config(text="Email/Username:")
lbl_password.config(text="Password:")

#Canvas
canvas.create_image(100,100, image=img_lock)

#Text
txt_email.insert(0, "example@email.com")

#Button
btn_add.config(text="Add", command=save_passord)
btn_gen_pw.config(text="Generate Password", command=generate_pw)
btn_search.config(text="Search", command=search)

#####Positions
#line 1 
canvas.grid(column=1, row=0)

#line 2
lbl_webSite.grid(column=0, row=1)
txt_web_site.grid(column=1, row=1)
btn_search.grid(column=2, row=1)

#line 3
lbl_email.grid(column=0, row=2)
txt_email.grid(column=1, row=2, columnspan=2)

#line 4  
lbl_password.grid(column=0, row=3)
txt_password.grid(column=1, row=3)
btn_gen_pw.grid(column=2, row=3)

#line 5
btn_add.grid(column=1, row=4, columnspan=2)

#Mainloop
window.mainloop()
