# Day 26 - List Comprehension and the NATO Alphabet

## List Comprehension
- List comprehension in Python is a way of creating a new list from another list in a much simpler way than using a for loop.
- This uses the format of `new_list = [new_item for item in list]`

Using this format instead of this:
```python
numbers = [1, 2, 3]
new_list = []
for n in list:
    add_1 = n + 1

new_list.append(add_1)
```
We could use this one line of code instead:
```python
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
# Our new list now would be new_list[2, 3, 4]
```
- You can also use the same format for other sequences like strings, dictionaries, tuples, ranges
```python
name = "Bob"
name_list = [letter for letter in name]
# Name list would be ["b", "o", "b"]
range_list = [num * 2 for num in range(1, 5)]
# Range list would be [2, 4, 6, 8]
```

## Conditional List Comprehension
- You can also create lists using conditions using the format `new_list[new_item for item in list if test]`
```python
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_name = [name for name in names if len(name) < 5]
# short_name now would be ["Alex", "Beth", "Dave"]
```
## Dictionary Comprehension
- Ditionaries can also be used with comprehension using this format
```python
new_dict = {new_key:new_value for item in list}
```
- You can also create a new dictionary based on the values of an existing dictionary
```python
new_dict = {new_key:new_value for (key, value) in dict.items()}  
```
For example we could use our list of names to create a dictionary with the students as the key and a random int between 1-100 as the value:
```python
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:random.randint(1, 100)for student in names}
```
Now let's take that dictionary and create a dictionary with students that passed:
```python
student_scores = {
    "Alex": 51,
    "Beth": 72,
    "Caroline": 62,
    "Dave": 81,
    "Eleanor": 38,
    "Freddie": 89
}

passed_students = {student:score for (student, score) in student_scores.items() if score >= 60 }
```

## How to Iterate Over a Pandas DataFrame

- DataFrame's can also be looped through the same way you loop through a dictionary, or using the `.itterows()` method
```python
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(value)

# Looping through DataFrames
student_data_frame = pandas.DataFrame(student_dict)
for (key, value) in student_data_frame.items():
    print(value)

# Loop through rows of DataFrame
for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.student)
    print(row.score)
```