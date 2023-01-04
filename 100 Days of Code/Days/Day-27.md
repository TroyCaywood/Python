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
- And then we'll display that label using the packer function `.pack()` which automatically places the label on the screen and centers it
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
