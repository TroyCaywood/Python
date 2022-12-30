# Day 24 - Files, Directories and Paths

- Today we will be working with files, directories and paths and using that knowledge to create a custom mail merge project

## Add High Score to Snake Game
- Let's add a high score tracker to our snake game that will stay even after you close the game.
- We'll do this using python to create a file that the high score saves to since the high score gets reset every time we run the code otherwise

### Reading and writing files in python
- Python has a built in method to open files called `open` then once the file is open you can use the `read()` method to get the contents of the file as a string
- Let's say we have a text file with "Hello my name is Bob." saved in it.
- If we wanted to read this file and then print out the contents we would do this:

The console would print `Hello my name is Bob.`
```python
with open("my_file.txt") as file:
  contents = file.read()
  print(contents)
```
- After opening a file and doing whatever you are doing with it, it's important to make sure you `close()` the file if you set the `open()` method to a variable to free up the resources that are being used to open and read that file. It's easier if you use `with open("file.txt) as variablename:` instead and then put all of your file modifications in the indented portion because it will automatically close the file that way.

- You can also modify a file using python using the `write()` method. When doing this you have to make sure to set the mode on the `open()` function to "w" for write. However, this will overwrite anything in the file. If you just want to add to the file, change the mode to "a" for append.
Here we add the string "New text." to our file:
```python
with open("my_file.txt", mode="a") as file:
  file.write("\nNew text.")
 ```
 
- One thing to note, if you try to open a file that doesn't exist in write mode, python will create that file for you.

- Now lets use this new knowledge to add a high score to our snake game.
- We've already created a way to reset the snake and gotten rid of the game over method, but I'm not going to cover that here since it doesn't relate to what we're doing.
- First we'll create a file called data.txt with the number 0 in that file
- Now in our Scoreboard class we'll read that file and set the `self.high_score` variable to the contents of that file
```python
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
```

- Then to save the new high score back to the data.txt file we'll update the `reset(self)` method of the Scoreboard class
```python
   def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
```
- Now our high score stays even if you close the program completely!

## Relative vs Absolute directories
- When working with directories in python, you can use absolute or relative formats
- An absolute directory would be the full path to the directory ex: c:\users\bob\desktop\text.txt in Windows or /users/bob/desktop/text.txt on Mac. When writing your code in python, python wants / characters rather than \ so use those even in windows directories.
- A relative directory would be "relative" to your working directory. IE where the file you are editing in pyton currently exists.
- So say you had a file in /users/bob/desktop/files/file.txt and your python file was in /users/bob/desktop the relative directory would be ./files/file.txt
- If you need to access a file that is above your working directory you use ../
- Say you had a file in /users/bob/file.txt and your python working directory is /users/bob/desktop/workdir you would use ../../file.txt as a relative path.

## Day 24 [Code Challenge](https://github.com/TroyCaywood/Python/tree/main/100%20Days%20of%20Code/CodeChallenges/Day-24) - Mail Merge - Do NOT click before you attempt on your own!


                
