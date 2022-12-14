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

