import tkinter as tk
from tkinter import Canvas
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
data_frame = pandas.DataFrame(data)
data_dict = data_frame.to_dict(orient="records")
print(data_dict)



def random_word():
    canvas.delete()
    word = random.choice(data_dict)
    canvas.create_text(400, 263, text=f"{word}", font=("Ariel", 40, "italic"))

window = tk.Tk()
window.minsize(width=800, height=526)
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=810, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

x_image = tk.PhotoImage(file="images/wrong.png")
x_button = tk.Button(image=x_image, highlightthickness=0)
x_button.grid(column=0, row=1)

check_image = tk.PhotoImage(file="images/right.png")
check_button = tk.Button(image=check_image, highlightthickness=0, command=random_word)
check_button.grid(column=1, row=1)


window.mainloop()



