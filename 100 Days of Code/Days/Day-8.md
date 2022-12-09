# Day 8 - Function Parameters & Caesar Cipher

- Functions can have inputs by creating variables inside of parenthesis
```python
def my_function(something):
  # Do this with something
  # Then do this
  # Finally do this
```
For example:
```python
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
  print(f"Isn't the weather nice today, {name}?")

# When we call greet with name we pass a string
greet_with_name("Bob")

# This would print:
# Hello Bob
# How do you do Bob?
# Isn't the weather nice today, Bob?
```
- In a function, the variable that we create inside the parenthesis is called the **Parameter** (the name of the variable) and the value that you set the parameter to when calling it is called the **Arguement** (the set value of the variable)

**Positional Arguements**

- Functions can have more than one parameter by adding a comma and adding the next parameter

Taking our last example and adding a location parameter
```python
def greet_with_name(name, location):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
  print(f"Isn't the weather nice in {location} today, {name}?")

# Now when we call greet with name we pass it two strings separated by a comma for the arguements
greet_with_name("Bob", "California")

# This would print:
# Hello Bob
# How do you do Bob?
# "Isnt the weather nice in California today, Bob?"
```
- Our example would be called a **Posistional arguement** because we don't specify which parameter we want to associate the arguements with so it always goes in the order that they were defined. The first parameter will always be the name, and the second parameter will always be the location in our example. This is the default way of calling a function.
- You can have more than two arguements in your function

**Keyword Arguements**

- When calling a function, rather than just putting in the arguement, you can specify the keyword you are defining with  the keywoard and an = followed by your arguement

Taking our previous example, but reversing the order using a keyword arguement.
```python
def greet_with_name(name, location):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
  print(f"Isn't the weather nice in {location} today, {name}?")

# Now when we call greet with name we pass it two strings separated by a comma for the arguements
greet_with_name(location="California", name="Bob")

# This would print:
# Hello Bob
# How do you do Bob?
# "Isnt the weather nice in California today, Bob?"
```
- Calling your functions this way is more accurate, but makes your code longer since you have to specify the keywords.


