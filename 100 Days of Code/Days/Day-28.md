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

- It's time to finish our user interface portion by adding some buttons and labels. We'll use fg= to change the label text color
```python
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"))
reset_button.grid(column=2, row=2)

checkmark = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark.grid(column=1, row=3)

window.mainloop()
```
Now our program looks a little better!

![image](https://user-images.githubusercontent.com/52113778/211099799-a58fc436-4a39-4752-bbfe-d389c8c2d0ae.png)

- To make our timer actually do something, we need to create some functions.
- We will user the `after()` method on our window object to call a count_down function that takes a count as an argument
- Then we'll create `start_timer` function that calls the `count_down()` function and assign that to our button using command=start_timer on the button object assignment
```python
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)
        
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)

```
- Now our timer counts down from 5 to 0 when we hit start

![python_25FjZB6WSO](https://user-images.githubusercontent.com/52113778/211104167-b7fcc00f-aee6-4f64-a2a3-80eb952f9d20.gif)

- We need to change our timer so it counts down from 5 minutes instead of 5 seconds and displays minutes and seconds while counting down
- We'll do this by taking 5 * 60 in the count, then we'll figure out the minutes and seconds by creating two variables
- `count_min = math.floor(count / 60)` the `math.floor()` rounds down to the largest whole number
- `count_sec = count % 60' this will give us the remainder after dividing by 60 which would be the seconds
- Then we'll change our timer text to an f-string to show our new variables every 1000 milliseconds
```python
def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # Math.floor returns largest whole number
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)

```

![python_8uoyQxAeJq](https://user-images.githubusercontent.com/52113778/211106000-307b09d1-7a21-4d90-9690-7d57ef760aa4.gif)

- The counter looks mostly correct now, but we need to fix the timer so it says 5:00 instead of 5:0

## Dynamic Typing
- In Python we can set variables to strings or integers or booleans etc, but we can also dynamically change them
- For example
```python
a = 5
print(a)
print(type(a))
# 5 would print
# a is type int

a = "hello"
print(a)
print(type(a))
# Hello would print
# a is type string
```

- Using that knowlege, we can dynamically change our seconds from an integer to a string when `count_sec` is 0
```python
def count_down(count):
    # Math.floor returns largest whole number
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
```
- Now our timer looks correct when counting down!

![python_vSPANGkxvK](https://user-images.githubusercontent.com/52113778/211107574-0f7055d4-ad2d-40bb-a3e7-5a360fba3c31.gif)

# Changing Timer
- Now we need to change the timer based on the number of repetitions
- We'll do this by adding a global variable called reps and increasing it every time `start_timer()` is called
- Then we'll use modulo to test if the reps divides cleanly by 2 then we'll take a short break. If it is equal to 8 we'll take a long break, otherwise it will do the full 25 min timer.
```python
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
    else:
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    # Once timer reaches 0 call start_timer() again    
    else:
        start_timer()
```

- Now let's deal with adding a checkmark for every pomodoro completed, and setup a reset function that resets the program back to 00:00
- First we'll remove the `text=` argument from our checkmark object and we'll create a marks variable in the `start_timer()` that is set to an empty string
- Then we'll divide the current sessions by 2 so for every two sessions we will add a checkmark to the marks variable
- Then we assign the marks variable to `checkmark.config(text=marks)` to apply it to our checkmark object
```python
    # Once timer reaches 0 call start_timer() again
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmark.config(text=marks)
```

- To reset everything to default we'll call the global reps variable and then set it to 0
- Now we'll set `window.after_cancel(timer)` to stop the `window.after()` timer.
- Then we'll set `timer_label.config(text="timer")`
- Then we'll change `checkmark.config("text="")` so we have a blank string again
- Now we just have to assign `command=reset_timer` to our reset button to make the button function
```python
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    
```
- Now we have a functional pomodoro timer!

## Day 28 - [Code Challenge](https://github.com/TroyCaywood/Python/tree/main/100%20Days%20of%20Code/CodeChallenges/Day-28) - Pomodoro Timer - This was all covered in the videos, but you can take a look at the final code