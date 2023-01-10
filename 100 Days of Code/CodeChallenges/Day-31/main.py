import tkinter as tk
from tkinter import Canvas

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.minsize(width=800, height=526)
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_canvas = Canvas(width=810, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = tk.PhotoImage(file="images/card_front.png")
card_canvas.create_image(403, 263, image=card_image)
card_canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
card_canvas.grid(column=0, row=0, columnspan=2)

x_image = tk.PhotoImage(file="images/wrong.png")
x_button = tk.Button(image=x_image, highlightthickness=0)
x_button.grid(column=0, row=1)

check_image = tk.PhotoImage(file="images/right.png")
check_button = tk.Button(image=check_image, highlightthickness=0)
check_button.grid(column=1, row=1)






window.mainloop()