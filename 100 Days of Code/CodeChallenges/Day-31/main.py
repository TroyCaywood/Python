from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

data_frame = pandas.DataFrame(data)
data_dict = data_frame.to_dict(orient="records")




def new_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data_dict)
    canvas.itemconfig(current_canvas, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(current_canvas, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word["English"], fill="white")


def learned_word():
    data_dict.remove(random_word)
    data_dict_df = pandas.DataFrame(data_dict)
    data_dict_df.to_csv("data/words_to_learn.csv", index=False)
    new_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=810, height=530)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
current_canvas = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, text="Title", font=("Courier", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=new_card)
x_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=learned_word)
check_button.grid(column=1, row=1)

new_card()
window.mainloop()
