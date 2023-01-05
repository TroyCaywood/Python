# Day 27 - Tkinter, *args, **kswargs and creating GUI Programs

## Tkinter
- The [Tkinter](https://docs.python.org/3/library/tkinter.html) module is used for creating [GUIs](https://en.wikipedia.org/wiki/Graphical_user_interface) for python programs
- We can create a window in tkinter by using the `.Tk()` method and `.mainloop()`
- `.mainloop()` is what allows the window to stay open once created and also listens for user inputs and also must always be at the very end of your program
```python
import tkinter

# tkinter main window object
window = tkinter.Tk()
# Tkinter loop that keeps window open
window.mainloop()
```
- Now we have a nice little window with not much going on in it that stays open until we close it
 
![image](https://user-images.githubusercontent.com/52113778/210645765-a5273af5-113a-48ed-8cb7-0e6128c57d5f.png)

- Let's add some more components to our window
- We'll change the window's minimum size to 500x300 using `.minisize()`
- Add a title to the titlebar using `.title()`
- Add a label with some text by creating a `tkinter.Label()` object
- And then we'll display that label using the [packer](https://docs.python.org/3/library/tkinter.html#the-packer) function `.pack()` which automatically places the label on the screen and centers it
```python
import tkinter

# tkinter main window object
window = tkinter.Tk()

# Change window title
window.title("My First GUI Program")

# Change window minimum size
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))

# Place label on screen and center label
my_label.pack()



# Tkinter loop that keeps window open
window.mainloop()
```
Now our window looks like this:

![image](https://user-images.githubusercontent.com/52113778/210647322-eadec500-dad0-448e-9a27-a8f9adf29778.png)

## Default Values
- Some functions and methods have default arguments with pre-set values.
- Those functions may still have required arguments
```python
def my_function(a=1, b=2, c-3):
    # Do this with a
    # Then do this wih b
    # Then do this with c

# Change value of b parameter
my_function(b=5)
```
- In the above example, `my_function()` function has default values for a, b, and c.
- We can still change the values for any of those parameters, for example `my_function(b=5)`, but the other parameters will stay as their default values `(a=1, c=3)`

## *args - Unlimited Arguments
- Functions can be created to allow any number of arguments as the input using `*args`
- You don't have to use the word args, you can use a name of your choice, the `*` is the important part
```python
def add(*args):
    for n in args:
        print(n)
```
- Let's look at a real example. We'll create a function that will add together any number of arguments that we input
```python
def add(*args):
    print(sum(args))


add(2,3)
add(4, 6, 7)
add(77, 89, 800, 88, 773, 23, 44, 55, 22, 44, 565)
# Results would be:
    # 5
    # 17
    # 2580
```
- The arguments in a `*args` function are stored in a tuple and can be treated as such when you are defining your function. They can be accessed by index number etc.

## *kwargs - Unlimited keyword arguments
- You can also create a function with unlimited keyword arguments using `**kwargs` which are stored in a dictionary
```python
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# This would print
    #{'add': 3, 'multiply': 5}
    # 25
```
- The above function takes 2 + 3, then takes the resulting 5 and multiplies it by 5 to get 25
- tkinter contains many kwargs because tkinter was converted from another language
- You can also create a class using kwargs
```python
class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GT-R")

print(my_car.make)
print(my_car.model)
# This would print:
    # Nissan
    # GT-R

```
- When using kwargs if you don't want your code to error if no kwargs are specified, it's better to use `.get()` since it will just return `None` instead of an error
```python
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")

print(my_car.make)
print(my_car.model)
# This would print:
    # Nissan
    # None
```

## Buttons, Entry, and Setting Component Options
- tkinter options can be set in [multiple ways](https://docs.python.org/3/library/tkinter.html#handy-reference)
- Let's change the text on our label:
```python
# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))

# Both of these do the same thing
my_label["text"] = "New Text"
my_label.config(text="New Text")
```
- Buttons can be created using the `.Button()` method
```python
# Button
button = tkinter.Button(text="Click Me")
button.pack()
```
- Now we have a button on our screen! (it doesn't do anything yet)

![image](https://user-images.githubusercontent.com/52113778/210665881-08c42436-d9f3-48cf-809e-aff4ab079702.png)

- To make our button work, we have to create a function and pass that function to the button using `command=`

```python
# Button
def button_clicked():
    print("I got clicked!")


my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.pack()

```

- Now whenever we click our button, it prints `I got clicked!` to the console.
- Let's use what we've learned to make the label text change when we click the button using either `my_label["text"] =` or `my_label.config(text="")`
```python
import tkinter

# tkinter main window object
window = tkinter.Tk()

# Change window title
window.title("My First GUI Program")

# Change window minimum size
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))

# Place label on screen and center label
my_label.pack()

# Button
def button_clicked():
    my_label.config(text="The button was CLICKED!")

my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.pack()


# Tkinter loop that keeps window open
window.mainloop()
```
- Now our label text changes when we click the button!

<img width="497" alt="AFEDEF7E-50DB-4BD9-89A8-3A61DFFAD75F" src="https://user-images.githubusercontent.com/52113778/210691075-37dbfd79-1ed8-446f-9c6c-4279138b00e3.png">

- We can also collect user input in our GUI using `tkinter.Entry()`
```python
# Input
my_input = tkinter.Entry()
my_input.pack()
```
- Now we have an input field!

<img width="497" alt="image" src="https://user-images.githubusercontent.com/52113778/210691566-b0bafdcd-a515-4c2f-95ab-1dd8a88f1d0d.png">

- Now we'll change the label text every time we enter something in the text box and click the button using the `.get()` method
```python
import tkinter

# tkinter main window object
window = tkinter.Tk()

# Change window title
window.title("My First GUI Program")

# Change window minimum size
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))

# Place label on screen and center label
my_label.pack()

# Button
def button_clicked():
    my_label.config(text=my_input.get())

my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.pack()

# Input
my_input = tkinter.Entry(width=10)
my_input.pack()


# Tkinter loop that keeps window open
window.mainloop()

```
- Now we can actually use the input that we type into the box

<img width="497" alt="image" src="https://user-images.githubusercontent.com/52113778/210692174-1c130c3f-afe2-4031-9423-d0df8f090a6d.png">

- There are many other things we can do with tkinter:
```python
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
```
- That gives us a window that looks like this:
- 
<img width="494" alt="image" src="https://user-images.githubusercontent.com/52113778/210693324-e7b9000d-52d4-45bb-8bea-e29914908971.png">
