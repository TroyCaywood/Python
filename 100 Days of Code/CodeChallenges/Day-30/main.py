from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for number in range(randint(8, 10))]
    password_symbols = [choice(symbols) for number in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    # Use .join to combine the password list into a string with an empty string as the separator
    password = "".join(password_list)
    # Use pyperclip to copy generated password to clipboard
    pyperclip.copy(password)
    # Insert into password field
    password_entry.insert(0, f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    email = email_user_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showinfo(title="Empty Fields", message="Please don't leave any empty fields!")

    else:
        try:
            with open("./data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("./data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("./data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #


def search():
    website = website_entry.get()
    try:
        with open("./data.json", mode="r") as data_file:
            # Convert to dictionary
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="No Data", message="No datafile found. Please create at least one entry.")
    else:
        # Look for website key in data
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            # Display found username and password
            messagebox.showinfo(title=website_entry.get(), message=f"Username: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Doesn't Exist",
                                message=f"Sorry, {website_entry.get()} doesn't exist in the database")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=200, height=200)
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=18)
website_entry.grid(column=1, row=1)

search_button = Button(text="Search", width=13, command=search)
search_button.grid(column=2, row=1)

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "@gmail.com")
email_user_entry.icursor(0)
email_user_entry.focus()

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

generate_pw_button = Button(text="Generate Password", command=generate_password)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()