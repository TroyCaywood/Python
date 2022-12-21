# Day 17 - The Quiz Project & the Benefits of OOP

## Creating your own classes
- Remember, a class is basically just a blueprint for creating objects
- We can also create our own classes.
- To create a class you use the class keyword followed by the name of your class in Pascal case (with the first letter of each word capitalized) then a colon and the contents of your class indented under that.

If we were to call test_class it would print "this is a class!"
```python
class NewClass:
  print("this is a class!)
  
 test_class = NewClass()
 ```
 
## Creating class attributes
- An attribute is a variable attached to an object. They are what the object will have variables associated with the final object.
- You can create new attributes by calling the object followed by a period and then the attribute name then equal sign and the value of the attribute.
```python
class User:
    pass


user_1 = User()
user_1.id = "001"
user_1.username = "bob"
```

## Constructor

- A constructor is a part of the class blueprint that allows you to specify what should happen when your object is being constructed. This is also known as **intializing** the object.
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
- To add attributes to your constructor, put the name of the parameter in the parenthesis after self with a comma init on the init line and then define the parameter by putting self.parameter = parameter. Normally the parameter will be equal to the name of the attribute, but that isn't a hard rule.
- Any arguements that you add to your constructor are required every time a new object is created.

Now we can create new user IDs and users just by making new objects
```python
class User:

   def __init__(self, user_id, username):
    self.id = user_id
    self.username = username
    print(f"Creating user ID: {self.id} with the Username: {self.username}")

user_1 = User("001", "Bob")
user_2 = User("002", "Bill")
```
- You can also set default values in your constructor definition that will apply to every object created

Now we've added a followers attribute and set it to 0. Notice that you do not have to add the attribute to the parenthesis since you aren't going to be changing it when the user is created.
```python
class User:

   def __init__(self, user_id, username):
    self.id = user_id
    self.username = username
    self.followers = 0
    print(f"Creating user ID: {self.id} with the Username: {self.username}")

user_1 = User("001", "Bob")

print(user_1.username)
print(user_1.followers)
```

- Methods can also be added to your init class. When adding a method, you must always add (self) to the definition since it tells the method what object it was called by.

Now we've created a new follow method that we can call on our objects to increase their follower/following counts.
```python
class User:

   def __init__(self, user_id, username):
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0
    print(f"Creating user ID: {self.id} with the Username: {self.username}")
    
    def follow(self, user):
      user.followers += 1
      self.following += 1

user_1 = User("001", "Bob")
user_2 = User("002", "Joe")

user_1.follow(user_2)
```
- The main benefit of OOP is it allows you to create an easily changable and updateable framework for your programs.
---
## Day 17 [Code Challenge](https://github.com/TroyCaywood/Python/tree/main/100%20Days%20of%20Code/CodeChallenges/Day_17-QuizGame) - Make sure you go through the whole video before clicking. You walk through this challenge together for the most part.


