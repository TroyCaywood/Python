import requests
import datetime as dt
import tkinter as tk
import tkcalendar
from tkinter import messagebox

USERNAME = "my_username"
TOKEN = "123124155"
GRAPH_ID = "graph1"

#-----------------CREATE USER-----------------#

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "1232141",
    "username": "my_username",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)


#-----------------CREATE GRAPH-----------------#

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Python Study Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


#-----------------POST PIXEL-----------------#

def post_pixel():
    time = dt.datetime.now()
    time_string = time.strftime("%Y%m%d")
    print(time_string)

    pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    pixel_data = {
        "date": f"{date.get_date()}",
        "quantity": f"{hours_spinbox.get()}",
    }

    pixel_request = requests.post(url=pixel_post_endpoint, headers=headers, json=pixel_data)
    messagebox.showinfo(title="Done", message=pixel_request.text)

#-----------------UPDATE PIXEL-----------------#


def update_pixel():

    pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.get_date()}"
    pixela_update_json = {
        "quantity": f"{hours_spinbox.get()}"
    }

    pixel_update_request = requests.put(url=pixel_update_endpoint, headers=headers, json=pixela_update_json)
    messagebox.showinfo(title="Done", message=pixel_update_request.text)

#-----------------DELETE PIXEL-----------------#


def delete_pixel():
    pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.get_date()}"

    pixel_delete_request = requests.delete(url=pixel_delete_endpoint, headers=headers)
    messagebox.showinfo(title="Done", message=pixel_delete_request.text)


window = tk.Tk()
window.title("Pixela Updater")
window.minsize(width=300, height=300)
window.config(pady=20, padx=20)

date_label = tk.Label(text="Choose a date:")
date_label.grid(column=0, row=2)

date = tkcalendar.Calendar(date_pattern="ymmdd")
date.grid(column=1, row=2, rowspan=2)
# date.config(padding=1)

hours_label = tk.Label(text="How many hours did you study: ")
hours_label.grid(column=0, row=0)

hours_spinbox = tk.Spinbox(from_=0, to=99)
hours_spinbox.grid(column=1, row=0, pady=10)

radio_select = tk.IntVar()

update_radio = tk.Radiobutton(text="Update Pixel", variable=radio_select, value=1)
update_radio.grid(column=1, row=4)

new_radio = tk.Radiobutton(text="Create Pixel", variable=radio_select, value=2)
new_radio.grid(column=0, row=4)

delete_radio = tk.Radiobutton(text="Delete Pixel", variable=radio_select, value=3)
delete_radio.grid(column=3, row=4)


def pixela_button():
    if radio_select.get() == 2:
        post_pixel()
    elif radio_select.get() == 1:
        update_pixel()
    elif radio_select.get() == 3:
        delete_pixel()


update_button = tk.Button(text="Update/Create Pixel", command=pixela_button)
update_button.grid(column=1, row=5)

window.mainloop()
