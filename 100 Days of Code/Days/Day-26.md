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
