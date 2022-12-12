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
In this example we are finding the highest score in a list. We do this by creating a variable called max set to 0 and then creating a for loop that says if the score in the student_scores list is greater than the value in max, change max to that score. Then we print the result. This could also be done using print(max(student_scores))
```python
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0

for score in student_scores:
    if score > max:
        max = score

print(f"The highest score in the class is: {max}")
```
## For loops and the range function

- You can use a for loop without pointing to a list using the range function.
Notice that it doesn't include the last number in the range. If you truely wanted the numbers 1-10 you would have to use range(1, 11)
```python
for number in range (1, 10):
  print(number)
  
 1
 2
 3
 4
 5
 6
 7
 8
 9
 ```
 - If you want to count by a number other than one you can add another comma with and then the step size
 
 ```python
 for number in range(1, 11, 3):
  print(number)
  
  1
  4
  7
  10
  ```
 If you wanted to find the total sum of all even numbers between 1 and 100 you could write something like this:
  ```python
even_numbers = 0

for number in range(2, 101, 2):
    even_numbers += number

print(even_numbers)

2550
```
[FIZZBUZZ!](https://en.wikipedia.org/wiki/Fizz_buzz) Notice that we have to write the fizzbuzz if statement first, because otherwize it would stop at fizz or buzz since both of those statements are true.
```python
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```
---

## Day 5 [Code Challenge](https://github.com/TroyCaywood/Python/blob/main/100%20Days%20of%20Code/CodeChallenges/Day_5_Randpassgen.py) - Don't click if you are going to attempt yourself first.
