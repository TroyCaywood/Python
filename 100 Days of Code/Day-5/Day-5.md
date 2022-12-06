# Day 5 - Python Loops

---

## For Loops

- A for loop can be used to perform an action to each item in a list. A loop allows you to easily execute the same section of code multiple times.

```python
for (name of sigle item in list) in (list name):
  do action
  more actions
  even more actions
````
For example, this for loop runs through the fruits list and assigns the variable name "fruit" to the first index "Apple" and then prints the fruit variable which is now "Apple". It then starts over for Peach and then Pear and would continue on to the end of the list if there were more items in the list.
```python

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
  print(fruit)
  

Apple
Peach
Pear
```

- Pay attention to the indentation when writing your for loops. Anything indented below the for line will run inside the loop. As soon as you start writing code not indented after the for loop, you are no longer inside of the loop.
- For loops will run for however many items are in the list.

In this example we create a list of student heights and then find the average. First we create two variables called total_height and students and set their values to 0. Then we create a for loops for the heights and add each to the total_height variable to get the total height. Then we write a for loop that adds 1 to the student variable for every index in the list. Finally we print total_height divided by students to get the average height for the given list.
```python

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
students = 0

for height in student_heights:
    total_height += height

for student in student_heights:
    students += 1



print(round(total_height / students))

Input a list of student heights
156 178 165 171 187

171
```
