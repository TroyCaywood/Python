# Day 28 - Tkinter, Dynamic Typing, and the Pomodoro GUI Application

- Today we will be building a [Pomodoro timer](https://en.wikipedia.org/wiki/Pomodoro_Technique)
- In order to do that we will use tkinter to build our interface

## tkinter Canvas Widget
- The tkinter canvas widget allows you to layer things one on top of the other such as images
- First we'll have to create a `Canvas()` object
- Then we'll create a `PhotoImage` object to convert our png of a tomato to a PhotoImage that canvas can use
- Finally we'll tell Canvas to create the image and where to display it on the screen
```python
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50)


canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
canvas.pack()




window.mainloop()
```
- Now we have a nice picture of a tomato when we run our program!

![image](https://user-images.githubusercontent.com/52113778/211095820-283e60a2-71e4-4633-a200-3a5e9ecae7f2.png)

- Let's add the starting text for our timer using `canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))`
- This will create our text at x=103 y=130 with the text 00:00 using our courier font at 35 in bold.

![image](https://user-images.githubusercontent.com/52113778/211096659-58e28a9a-0a50-4be3-952c-e7da9a39fb97.png)

- Now lets change our background to the YELLOW constant using `bg=YELLOW` on both `window.config()' and `Canvas()`

![image](https://user-images.githubusercontent.com/52113778/211097471-1c20db6a-6a06-470c-ab11-96a5b853076c.png)


![image](https://user-images.githubusercontent.com/52113778/211099799-a58fc436-4a39-4752-bbfe-d389c8c2d0ae.png)



