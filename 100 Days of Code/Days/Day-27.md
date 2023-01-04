# Day 27 - Tkinter, *args, **kswargs and creating GUI Programs

## Tkinter
- The [Tkinter](https://docs.python.org/3/library/tkinter.html) module is used for creating [GUIs](https://en.wikipedia.org/wiki/Graphical_user_interface) for python programs
- We can create a window in tkinter by using the `.Tk()` method and `.mainloop()`
- `.mainloop()` is what allows the window to stay open once created
```python
import tkinter

# tkinter main window object
window = tkinter.Tk()
# Tkinter loop that keeps window open
window.mainloop()
```
- Now we have a nice little window with not much going on in it that stays open until we close it
 
![image](https://user-images.githubusercontent.com/52113778/210645765-a5273af5-113a-48ed-8cb7-0e6128c57d5f.png)
