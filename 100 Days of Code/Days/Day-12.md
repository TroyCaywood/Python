# Day 12 - Scope & Number Guessing Game

## Namespaces Local VS Global Scope
### Scope

#### Local Scope
- Local scope exists within functions

In this example we define a function called drink_potion and create a variable called potion_strength that is set to 2. When we call the function it prints 2, but if you try to print the potion_strength variable you get a name error. That's because the potion_strength variable only is accessible from within the drink_potion function. It is in the drink_potion's local scope.
```python
# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

# This would print 2 and then a name error
```
### Global Scope
- Global scope is something that exists at the top level of a file. Top level meaning it is not within a function. A global variable can be called anywhere even in nested functions.

In this example we define a player_health variable and then print it within a function. We are able to do this since the variable's namespace is global.
```python
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

# This would print 10
```
- The concept of scope applies to anything that you assign a name to. The scope is it's namespace. 

### There is no block scope
- Some programming languages have block scope where if you define a variable nested within an if, while, for block of code that variable would be within the local scope of the if, while, for block. In python that is not the case.

In this example, new_enemy is nested within an if statement, but you can still call the new_enemy variable outide of the if statement because there is no block scope for if statements in python.
```python
# No block scope
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
# This would print Skeleton
```
If we change the code to be a function, we can no longer call the new_enemy variable because functions have local scope within them. Now we would get a name error.
```python
# No block scope
game_level = 3
def create_enemy:
    enemies = ["Skeleton", "Zombie", "Alien"]

    if game_level < 5:
        new_enemy = enemies[0]

print(new_enemy)
# This would give us a name error.
```
### Modifying a global variable

In this example, even though we see two instances of the variable "enemies", different values are printed when we call the enemies variable inside the function versus outside the function. That is because they are really two completely separate variables that just happen to be named the same. The enemies within the increase_enemies function is only accessible from within that function. It's not a good idea to name local and global variables the same thing.
```python

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# This would print enemies inside function: 2 enemies outside function: 1
```
- If you wanted to modify a global variable from within a function (local scope), you must first call the variable using global and then the variable name

This time we call the global enemies variable, increase it by 1 and then print the enemies variable. Then we print it outside the function and they both print 2 since we modified the global variable this time.
```python

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# This would print enemies inside function: 2 enemies outside function: 2 
```
- Modifying a global variable from within a local scope isn't a great idea since it can be hard to troubleshoot and is prone to errors.

The better way to do our previous example would be by returning the enemies variable within the function and add 1 and then set the variable to our function name to call it and increase the value by 1. That way you can move the function anywhere in your code without causing any issues.
```python

enemies = 1

def increase_enemies():
    return enemies + 1
    print(f"enemies inside function: {enemies}")

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# This would print enemies inside function: 2 enemies outside function: 2 
```

### Global Constants
- Global constants are variables that you define, but you never plan on changing again. EX: The value of pi (3.14159).
- When defining a global constant, the naming convention is to use all uppercase for the variable name. This is to remind you not to modify that variable within your code.

```python
# Global Constants
PI = 3.14159
URL = "https://www.google.com"
```
