# Day 5 - Python Loops

---

## For Loops

- A for loop can be used to perform an action to each item in a list

```python
for (name of sigle item in list) in (list name):
  do action
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
