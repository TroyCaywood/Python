# Day 29 - Building a Password Manager GUI App with Tkinter

- Today we are going to be building a password manager program with a GUI using tkinter
- First we'll create our canvas with the background image
```python
from tkinter import *

window = Tk()
window.minsize(width=200, height=200)
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=1)


window.mainloop()
```
- Some of our elements need to go across more than one column. To do this we'll use the `columnspan=` property of `grid()`. You set columnspan to the number of columns you want that object to go across
```python
from tkinter import *


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

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

generate_pw_button = Button(text="Generate Password")
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
```
- Now we have our interface setup and looking pretty decent

![image](https://user-images.githubusercontent.com/52113778/211211013-80a29be2-564c-41d2-a637-32ea4fbe413b.png)

- Let's change the program so the cursor is automatically in the website entry field when it is launched by using the `.focus()` function
- We'll also create a function to save our data to a txt file and then assign that to the add button command
- After the function saves the passwords to a file it will clear the website and password fields using the `.delete()` tkinter method. This method takes a start and end index value to tell it what to delete. Since we want to delete everything, we'll do 0 to END
```python
def save_password():
    with open("./data.txt", mode="a") as data:
        data.write(f" Website: {website_entry.get()} | Username: {email_user_entry.get()} | "
                   f"Password: {password_entry.get()}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
```

## Dialogs and Pop-Ups in tkinter
- It would be nice to have a pop-up dialog that confirms the password was saved. Let's learn about that now
- We can create a **standard dialog** using the `tkMessageBox` module
- We'll handle this by checking the length of the entries in the website and password fields
```python
def save_password():
    # Check length of password and website fields to make sure they aren't blank
    if len(password_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showinfo(title="Empty Fields", message="Please don't leave any empty fields!")
    # If they aren't empty go ahead and ask if the entered info is ok and save the entry
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \n"
                                                            f"Email: {email_user_entry.get()} \n"
                                                            f"Password: {password_entry.get()} \nIs it OK to save?")

        if is_ok:
            with open("./data.txt", mode="a") as data:
                data.write(f" Website: {website_entry.get()} | Username: {email_user_entry.get()} | "
                           f"Password: {password_entry.get()}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
```
## Create a random password
- All we have left now is making the generate password button work
- Lets create a function to do that
- First we'll clear any existing passwords in the password field
- We'll create 3 lists with letters, numbers, and symbols
- Then we'll create 3 new lists using list comprehension to pick random values from those lists
- Then we'll combine those lists using `.join`
- Then we'll copy that value to the clipboard using the pyperclip module
- Finally, we'll insert that password into the password field
```python
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
```