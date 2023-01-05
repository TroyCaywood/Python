import tkinter

# Create window and min size, padding, and title
window = tkinter.Tk()
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)
window.title("Miles to KM")

# Create labels
equal_label = tkinter.Label(text="is equal to:")
equal_label.grid(column=0, row=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

answer_label = tkinter.Label(text="0")
answer_label.grid(column=1, row=1)

km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)

# Create input box
input_box = tkinter.Entry(width=3)
input_box.grid(column=1, row=0)
input_box.insert(index=0, string="0")

# Create calculate function for button
def calculate():
    do_calc = int(input_box.get()) * 1.609
    # Change answer_label text to do_calc
    answer_label.config(text=f"{do_calc}")

# Create button and set command to calculate function
calc_button = tkinter.Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)



window.mainloop()
