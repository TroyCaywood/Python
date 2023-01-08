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

