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
- 
