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