# Day Four - Randomisation and Python Lists

---
## Modules
- A module is a file containing a set of functions you want to include in your application.
- For example, you could create a file called my_module.py containing this code:
```python
pi = 3.14159246
```
- To use the module, you would just have to add import my_module to the code you are writing. You could do things like:
```python
print(my_module.pi)
```

## Randomization

- Python has a [module](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences) available for generating randomness called "random"
- You must import the module before being able to use it

This code example will generate a random number between 1 and 10 every time random_integer is called.
```python
import random

random_integer = random.randint(1, 10)
print(random_integer)
```
- You can also generate a random float using random.random(), however it will only give you a float between 0 and 1 (**NOT** including 1)
- If you wanted to generate a float that was larger than 1, you can multiply random.random() by the ending integer. 0 to 5 in this example.
```python
import random

randomFloat = random.random() * 5

print(randomFloat)
```
You could use this to do something like make a random heads or tail generator
```python
import random

coin = random.randint(0, 1)

if coin == 1:
    print("Heads")
else:
    print("Tails")
```

---

## Lists
- A list is a data structure, a way of organizing and storing data
- Lists allow you to store and order grouped pieces of data
- Lists items are separated by commas and always contained within []

Here is a list of states ordered US by the date they entered the union.
```python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
```
- To extract a specific index from a list, you would call the name of the list followed by [] with the index number of the item you are wanting. 
```python
states_of_america[4]
```
-  To pull the first state you would do something like print(states_of_america[0]) as lists always start with 0 for the first item. This would print "Delaware" print(states_of_america[50]) would print "Hawaii"
- The beginning of a list is 0 because it is the beginning of the list, the next item is 1 because it's 1 away from the beginning of the list etc.
- If you call a negative number index, it will count from the end of the list states_of_america[-3] would be Arizona. -1 is the last item in the list.
- You can also change items in a list
```python
states_of_america[1] = "Pencilvania"
```
- To add an item to the end a list use .append
This would add "Troylad" as the last index in the list of states_of_america
```python
states_of_america.append("Troyland")
```
- There are [many](https://docs.python.org/3/tutorial/datastructures.html) other ways you can manipulate lists

```python
# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# import random module
import random

# Count how long the length of list is
name_length = len(names)

# Get a random index value
random_index = random.randint(0, int(name_length))

# Use random index number to pull that name
random_name = names[random_index]

# Print the result
print(f"{random_name} is going to buy the meal today!")
```
**Index Error**
- When you try to pull an index number that is beyond what is actually in the list, you will get an index out of range error. For example, if you list had 50 entries, and you tried to do print(list[51]) you would get an error.

**Nested Lists*
- Lists can be nested inside each other.

```python
fruits = ["Pears", "Apples", "Kiwi", "Tomatoes"]
vegetables = ["Broccoli", "Spinach", "Kale", "Potatoes"]

healthy_stuff = [fruits, vegetables]

print(healthy_stuff)

[["Pears", "Apples", "Kiwi", "Tomatoes"], ["Broccoli", "Spinach", "Kale", "Potatoes"]]
```
In this examnple. When you type in 23, for example, it would put the X on the bottom middle square. This is because we are passing values into a nested list. First we are selecting index 2 (because we are subtracting 1 from the entered value) which gives us list "row3", then we are selecting index 1 (because we are subtracting 1 from the entered value again) in the row 3 list and setting that index to the string "X".
```python

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
~~~
