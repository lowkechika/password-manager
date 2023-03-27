from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def random_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(6, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 6)

    password_list0 = [choice(letters) for char in range(nr_letters)]
    password_list1 = [choice(symbols) for char in range(nr_symbols)]
    password_list2 = [choice(numbers) for char in range(nr_numbers)]

    password_list = password_list0 + password_list1 + password_list2

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email_username,
                          "password": password, }
                }

    if website == "" or password == "":
        messagebox.showinfo(title="Field Missing!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                print(data)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    global website_entry
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        website = website_entry.get()
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']} \nPassword: "
                                                            f"{data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)
window.maxsize(width=600, height=600)

canvas = Canvas()
canvas.config(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label()
email_username_label.config(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=52)
email_username_entry.insert(0, "jmtagare@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=52)
password_entry.grid(column=1, row=3, columnspan=2)

# Buttons
generate_password_button = Button()
generate_password_button.config(text="Generate Password", command=random_password, width=14)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
