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