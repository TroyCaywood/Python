# Day 34 - API Practice - Creating a GUI Quiz App

- Let's update our quiz app from a while back to use the actual API rather than copied data
- To do so we'll update the data.py file
```python
import json
import requests

# Parameters. 10 Questsion, Boolean type
parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

# We only want the results portion of the JSON since it contains all the questions
question_data = data["results"]
```
- Now every time we run our quiz program we get 10 new random questions every time!
- Some of the questions we get back look a little funny with weird symbols. This is because they are [HTML Entities](https://www.w3schools.com/html/html_entities.asp)
- To fix this we need to [unescape](https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string) that html code using the `html` module
- We'll edit our quiz_brain.py file importing the html module and adding a new `q_text = html.unescape(self.current_question.text)` variable
```python
  def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        self.check_answer(user_answer)
```
- Now the formatting in our questions looks correct again
- Let's create a quick user interface as a new class in the ui.py file
```python
from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.create_text(
            150,
            125,
            text="test Test",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()

```