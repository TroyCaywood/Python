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
- Now we create a QuizInterface object in main.py and when we run our program we have a nice interface to work with

<img width="335" alt="image" src="https://user-images.githubusercontent.com/52113778/212449353-144c9cf8-9183-447c-bdc7-418f8afa7847.png">

- Now that we have a UI and our questions coming from the API we need to tie the two together
- First let's change our quiz_brain `next_question()` method to return the question
```python
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
```
- Next we need to tell the ui.py to initialize the quiz_brain when the UI is created
```python
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
```

- Now we'll create a method within ui.py to show the next question on GUI
```python
   def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
```
- Then in main.py we just need to tell the QuizInterface to inialize the quiz `quiz_ui = QuizInterface(quiz)`
- Now our program actually show the questions in the GUI, they just don't wrap correctly yet
- To fix this we just have to add `width=280` to our canvas text
```python
self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="test Test",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
```
#### Type Hints

- When before declaring variables or when writing functions, you can specify the data type by using type hints
- Doing this will help you down the line if you have a long program and have forgotten what data type a variable or function wants
```python
age:int
name:str

age = 22
name = "Bob"
```
- If we tried to use a string for `age` or an int for `name`, we would now get an error
- You can do the same thing with functions
```python
def police_check(age: int):
    if age > 16:
        can_drive = True
    else:
        can_drive = False
    return can_drive
```

- You can also specify the output of a function by using `->` and then the data type
```python
def police_check(age: int) -> bool:
    if age > 16:
        can_drive = True
    else:
        can_drive = False
    return can_drive
```

- Now let's get our quiz app to let us check the answer by using the buttons on the GUI
- We'll create two new methods in our ui class that call the `check_asnwer` method from the quiz brain class and pass the strings True and False
```python
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
```

- Now lets add a method in ui.py that changes the background color to red or green depending on if the answer is right and then changes to the next question
```python
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        elif not is_right:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
```
- Now we'll change the `next_question()` method to change the score and change the background back to white
```python
  def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
```
- Next let's change the `get_next_question` method so the game actually ends correctly and make it so the buttons disable at the end
```python
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz."
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")                                              f"\nYour Score: {self.quiz.score}")
```

## Day 34 - [Code Challenge](https://github.com/TroyCaywood/Python/tree/main/100%20Days%20of%20Code/CodeChallenges/Day-34) - Today was walked through in the videos, but here is the final code if you want to have a look.
