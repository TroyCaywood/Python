# Day 16 - Object Oriented Programming (OOP)

### Procedural programming
- Procedural programming is Where you setup procedures or functions that do specific things. One procedure leads to another procedure and the computer works from top to bottom and jumps out to a function as needed.
- Because of the complexity of relationships between different functions and procedures, procedural programming becomes very hard to read and understand with longer more complex code.

## Object Oriented Programming (OOP)
- OOP is simplifying the relationships in your code to make it more scalable and managable for larger projects
- Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects. 
- Let's pretend we are creating a virtual restaurant. We'll have a chef, waiter, cleaner, and manager.
- So if we are going to model the waiter, we need to know what the waiter model has (attributes) and what it does (methods).
   + We could say whether the waiter is holding a plate and what tables they are responsible for.
   + Then we can say that they take orders and take payments:
```python
# Attributes (Has)

is_holding_plate = True
tables_responsible = [4, 5, 6]

# Methods (Does)
def take_order(table, order)
  # takes order to chef
def take_payment(amount):
  # add money to restaurant
```
- An **attribute** is a variable that is attached to a particular object
- A **method** is a function that a modeled object can do
- You can have multiple versions of objects generated from an object. This is called a **class**.
- A **library** is an umbrella term referring to a reusable chunk of code. Usually, a Python library contains a collection of related modules and packages.
- One example of a built in library is [turtle](https://docs.python.org/3/library/turtle.html). You can use it to draw graphics on the screen.

## Constructing objects and accessing their attributes and methods
- Creating a new object from a class:
- The class in an object is normally written in Pascal case. Meaning the first letter of each word in the class capitalized to differentiate it from variables etc.
- To create an object, you give the object a name, followed by equals and then the name of the class followed by parenthesis:
```python
# object = ClassName()
car = CarBlueprint()
```
- To access a method (a function that an object has) that an object has, you first type the object name followed by period and then the method that you're calling followed by parenthesis.
```python
car.stop()
```
- Python **packages** are basically a directory of a collection of modules.
- There are many free developer packages that can be downloaded online from [Pypi](https://pypi.org/) (python package index)
- You can install packages directly in Pycharm by going to file, settings, then go to your project, and click on python interpreter and then click the plus at the bottom of the screen and enter the name of the package you want to install then click on it and click install package.
- To change an attribute of an object, you type the name of the object plus a period followed by the attribute and then an equals sign and the value of the attribute
```python
myobject.align = "l"
```

---
## Day 16 [Code Challenge](https://github.com/TroyCaywood/Python/blob/main/100%20Days%20of%20Code/CodeChallenges/Day-16/CoffeeMachine-OOP.py) - Coffee Machine OOP - Do not click if you plan on attempting yourself!


