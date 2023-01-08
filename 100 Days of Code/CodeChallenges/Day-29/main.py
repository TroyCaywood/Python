from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open("./data.txt", mode="a") as data:
        data.write(f" Website: {website_entry.get()} | Username: {email_user_entry.get()} | "
                   f"Password: {password_entry.get()}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

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

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "@gmail.com")


password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

generate_pw_button = Button(text="Generate Password")
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()