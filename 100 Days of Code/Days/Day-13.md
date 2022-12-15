# Day 13 - Debugging: How to Find and Fix Errors in your Code

- EVERYONE creates bugs. Don't feel like you're a bad programmer because you found a bug.
- The first step is to describe the problem. It's hard to fix a bug if you don't understand exactly what the problem is.

When you try to run this code, nothing prints:
```python
# Describe Problem
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()
```
- Let's try to describe the problem:
  + What is the for loop doing
     + The for loop is going through a range of integers 1-20 one by one
  + When is the function meant to print "You got it"?
     + When i is equal to 20
  + What are your assumptions about i?
     + That i will reach 20

- So why isn't our code working? If you look at how the range function works, it takes a set of integers and goes from the first integer to one integer before the last. So since we have 1-20 in our range, the code only ever gets to 19 before the for loop stops and i never is equal to 20.
- We could fix this by changing our range to 1, 21 instead. That way for loop will go from 1 to 20.

Now our code will work correctly!
```python
# Describe Problem
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()
```
- When debugging your code, try to go through your list of assumptions about how your code should be working to figure out which one is actually false.

- When you have a bug that only happens sometimes, see if you can make it happen all the time to help you troubleshoot.

In this code we sometimes get an index out of range error for the print line.
```python
# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
```
- If we look at the docstring for the randint function we see that it returns a random integer in the range 1, 6 including 1 and 6.
 ![image](https://user-images.githubusercontent.com/52113778/207731947-c33c9d52-b11d-4c5e-81e4-9f0072749101.png)
 - What happens if we change the randint range to just 1? The code still works fine
 - What happens if we change the randint range to just 6? We get an index out of range error every time.
 - This is happening because the index for a list starts at 0 and our list only has six entries, so the last index is 5. Whenever randint would choose 6, we would get the index out of range error.
 - We can fix our code by changing randint's range to 0, 5. That way we will only get indexes that are in our list

## Play Computer

- Another strategy for debugging code is "playing computer"

In this code, if we put in 1994 for the input, nothing prints. Why?
Let's walk through the code and pretend we are the computer:
```python
# User inputs 1994. year = 1994
year = int(input("What's your year of birth?"))
# 1994 is greater than 1980 this statment is True, but it's not less than 1994, this statement is False. True and False combine to False. Statement is False.
if year > 1980 and year < 1994:
  print("You are a millenial.")
# 1994 is also not greater than 1994, this statement is false. No more lines of code left. Nothing prints.
elif year > 1994:
  print("You are a Gen Z.")
 ```
 - Walking through the code we can see that it isn't printing because 1994 is not less than 1994 and it is not greater than 1994. To fix our code, we need to add greater than or equal to 1994. That way putting 1994 in doesn't confuse the computer.
```python
# Input 1994. year = 1994
year = int(input("What's your year of birth?"))
# 1994 is greater than 1980 (True), but not less than 1994 (False). True and False = False
if year > 1980 and year 1994:
  print("You are a millenial.")
# 1994 is greater OR equal to 1994 (True). "You are a Gen Z." prints now
elif year >= 1994:
  print("You are a Gen Z.")
```
## Watch for red underlines
- When editing code in an editor. Watch for red unerlines. They point out errors in your code and if you hover over them will give you clues as to why your code isn't working.
- For errors you get in the console when running code, try searching on google for the error. More often than not, there will be a forum post somewhere that has the answer to your issue.

There are several errors in this code. The print line is underlined in the editor and says expected indent.
```python
# Fix the Errors
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")
```
After fixing the indent, the code still doesn't work right. We get an error in the console that says "TypeError: '>' not supported between instances of 'str' and 'int'" Searching for that error on google tells us you cannot compare a string to an integer. Age is only returning a string. We need to convert it to an integer.
```python
# Fix the Errors
age = int(input("How old are you?"))
if age > 18:
  print("You can drive at age {age}.")
```
Now we don't get any errors, but the print line doesn't print the number of the age. This is where experience and knowledge come in. We know that we need an f string in order for the variable to print in the print statement. If you didn't already know that, debugging would be a lot harder. You just have to keep trying.

Now our code works!
```python
# Fix the Errors
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")
```

## Print is your friend
- The print function can be very useful when debugging your code.
- It can be hard to tell what your code is doing sometimes without printing the results.
```python
In this code. No matter what numbers you put in, you always end up with an anwswer of 0. Without using print, it would be harder to figure out what is going on.
#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```
When we print pages and words per page we can see what is happening. Pages accepts our input and stores is fine, but words_per_page does not. It always is 0. If we look at the word_per_page line we have two = signs and that means we are checking if it is equal to int(input("Number of words per page: ")) and when we enter an input it will not be equal to that so it's False and gets set to 0. We simply need to delete the extra = sign..
```python
#Print is Your Friend
pages = 0
word_per_page = 0
# We input 10
pages = int(input("Number of pages: "))
# Print pages. Pages prints pages = 10
print(f"Pages = {pages}")
# We enter 10 again
word_per_page == int(input("Number of words per page: "))
# Print words_per_page prints word_per_page = 0.
print(f"word_per_page = {word_per_page}")
total_words = pages * word_per_page
print(total_words
```

## Use a debugger
- When you are really stuck, make sure you use a debugger to help you step through exactly what is going on with your code and find the errors. [Python Tutor](https://pythontutor.com) is a good online debugger.

# Final Tips
- Take a break! Sometimes staring at a problem for hours will get you nowhere. Stepping away and doing something else for a while and then coming back to the problem with a fresh set of eyes can make solving the problem much easier.
- Ask a friend! Ask someone else to look through your code and see if they can help you find the issue.
- Run often! Make sure you run your code often. Don't wait until you're at the very last item before you even try running your code. Make sure you test things as you add them by running your code. If you do end up with multiple bugs, try to tackle them one at a time.
- Ask stackoverflow! [Stack Overflow](https://stackoverflow.com) is a great resource for programmers and full of helpful people. You may even find your issue on there without having to ask a question even.
- Everyone gets bugs! Having bugs in your program doesn't mean you're a bad programmer. Every programmer ends up with bugs in their program. Becoming skilled at fixing them yourself is a skill in itself.

# No code challenge today.
