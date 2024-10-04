from textwrap import indent
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    #Using list comprehension

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    # print(type(password_list))

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    #pythonic way of doing this using join() method of the string...
    my_password = "".join(password_list)
    password_entry.insert(0,my_password)
    pyperclip.copy(my_password)

    # print(f"Your password is: {my_password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any field empty!" )
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data  = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# -------------------- Find the password (search functionality) --------------------------------#
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No email and password found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword = {password}")
        else:
            messagebox.showinfo(title = "Error",message=f"No details for {website} exists.")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.grid(column=1,row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=40)
username_entry.grid(column=1,row=2,columnspan=2)
username_entry.insert(0,"sabin@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

#Button
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=save_pass)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text = "Search", command=find_password,width=10)
search_button.grid(column=2,row=1)




window.mainloop()