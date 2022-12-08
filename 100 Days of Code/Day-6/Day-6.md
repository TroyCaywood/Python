# Day 6 - Python Functions


## Functions
- A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
- Python has many [built-in functions](https://docs.python.org/3/library/functions.html) for example:
  + int()
  + print()
  + range()
  + str()

**Defining and calling python functions**
- To defined a function, you use def functionname(input parameter, input parameter): followed by what you want the function to do.
- To call the function you would just type the function name and the parameters you want to pass to the function.

```python
#Define function name and parameters
def my_function():
  # Do this
  print("Hello)
  # Now do this
  print("Bye)

# Call the function
my_function()

# Function would output this:
Hello
Bye
```
**Indentation in Python**
- A block of code can be indented using "ctrl+]" in Windows. (] to unindent) 
- Indentation matters a lot in Python. Especially in functions. If the actions you are wanting to happen are not indented under the def statement, they will not run when the function is called.

```python
# This function would print "Hello" and "World" when called
def my_function():
  print("Hello")
  print("wWorld")
  
# This function would only print "Hello" because print("World") is not indented and therefore is OUTSIDE of the function
def my_function():
  print("Hello")
print("World")
```
- You can kind of think of it like the folder structure on a filesystem. If you have a set of files inside a folder and you are browsing to that folder, you can only see those files at that time. If you have another file outside of that folder, it is not visible to you. 
- You can use tab or four spaces to indent, but Python does not allow you to mix both in a file so choose one. Python documentation recommends four spaces rather than tab. Most editors will allow you to change tab to insert 4 spaces as well.

In this example you can think of the def portion followed by everything else as one container, the if functions with their print statements are two separate containers within the def container.
```python
def my_function():
  if sky == "clear":
    print("blue")
  elif sky == "cloudy":
    print("grey")
```

## While Loops
- A while loop will execute a set of statements as long as a condition is true.
```python
while something_is_true:
  #Do something repeatedly
  #do something else
  #etc
```
This code would print "You still have #of stuff stuff!" 6 times.
```python
# Define a variable called stuff and set it to 6
stuff = 6

# While stuff is greater than 0
while stuff > 0:
  print(f"You still have {stuff} stuff!")
  # Subtract 1 from stuff variable
  stuff -= 1
```
- For loops are better for working with lists and ranges when you care about where you are in the list and what item you're iterating etc
- While loops are better when you want to carry out a function many times until a condition that you set
- While loops can be a little more dangerous since you can create a loop that never becomes false and this creates an infinite loop where the code does not stop

---
## Day 6 - No real code challenge today. Play with [Reeborg](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json) and see if you can escape the maze using while loops and if elif else statements!
  
