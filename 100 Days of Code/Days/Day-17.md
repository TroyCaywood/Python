# Day 17 - The Quiz Project & the Benefits of OOP

## Creating your own classes
- Remember, a class is basically just a blueprint for creating objects
- We can also create our own classes.
- To create a class you use the class keyword followed by the name of your class in Pascal case (with the first letter of each word capitalized) then a colon and the contents of your class indented under that.

If we were to call test_class it would print "this is a class!"
``python
class NewClass:
  print("this is a class!)
  
 test_class = NewClass()
 ```
 
## Creating class attributes
- An attribute is a variable attached to an object.
- You can create new attributes by calling the object followed by a period and then the attribute name then equal sign and the value of the attribute.
```python
class User:
    pass


user_1 = User()
user_1.id = "001"
user_1.username = "bob"
```

## Constructor

- A constructor is a part of the blueprint that allows you to specify what should happen when your object is being constructed. This is also known as **intializing** the object.
- This allows you to set variables, counters, switches etc to their starting values.
- To create a constructor we use the init function
```python
Class Car:
  def __init__(self):
  # initialize attributes
```
- It's important to remember that the init function will be called any time you create a new object using that class

In this example, "new user being created.." will be printed twice since we are creating two new objects using the User class.
```python
class User:

   def __init__(self):
        print("new user being created...")

user_1 = User()
user_1.id = "001"
user_1.username = "bob"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "Joe"

print(user_2.username)
```

