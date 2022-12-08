# Day 3 - Conditional Statements, Logical Operators, Code Blocks and Scope

---

## Conditional Statements

**If/Else Statements**
- An If/Else statement runs a block of code if a statement is True, if the statement is False it runs the else block of code.

In this example, it would print "continue" since the water level is less than 80 and therefore the if statement is true. Notice the indentation on the print lines. This is important in python and tells the computer that it needs to run that line when the if or else statement is met. Think of the indented parts as living inside the if or else statement blocks. Also do not forget the ":" after the if and else statements.
```python
water_level = 50
if water_level > 80:
  print("Drain water")
else:
  print("continue")
```
- If/else statements can be nested inside one another.

In this example if the height entered is greater than 120 it will printer "You can ride the rollercoaster!" and enter the nested if/else statement that checks their age and gives a ticket price. If the number entered is less than 120 it skips the if print and the nested if/else statement and moves on to the else statement that prints "Sorry you have to grow taller before you can ride."
```python
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?"))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")
```
**Elif**
- Elif (else if) is used to check if multiple statements are true
We have added several more elif statements to check in the rollercoaster example now. If the computer gets to any of the elif statements and they evaluate as True, it will continue on to print the string contained in that elif statement. If the elif statement is False, it will continue on to the next elif statement.
```python
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?"))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  elif age == 22:
    print("Congratulations, you're 22!")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")
```

**Multiple If Statemnets in Succession**
- If statements can be used in succession. Compared to elif, multiple If statements evalute if the statement is True regardless of wether the prior If statement was True or not.

In this example, we create the variable bill and set it's value to 0 before entering our if statement. Then, the if statement evaluates their age and sets the value of bill according to their age. We then create the wants_photo input within the original if statement and add another if statement for Y that adds 3 to the value of bill and then prints the bill total. Note that the indentation of the if statements matters as far as when they run during the program.
```python
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
   #Add $3 to bill
   bill += 3
 
  print(f"Your final bill is {bill}")
   
else:
  print("Sorry, you have to grow taller before you can ride.")
```
  
## Comparison Operators
- There are different comparison operators that can be used to compare values in python
  + ">" Greater than
  + "<" Less than
  + ">=" Greater than or equal to
  + "<+" Less than or equal to
  + "==" Equal to
  + "!=" Not equal to
**Modulo**
- The modulo operator is used to give the remainder of a division equation. EX 4 % 2 = 0  and 99 % 2 = 1

## Logical Operators
- and - When using the and operator, both statements must be True for the line to evaluate as True. If just one condition evaluates as False, then the whole line is False.

```python
a = 12

a > 10 and a < 13
True

a > 10 and a < 11
False
```

- or - the "or" operator is used when you only need one statement to be True.

```python
a = 12

a > 10 or a < 7
True
```

- not - the "not" operator basically reverses a condition. If a condition is True it becomes False if a condition is False it becomes True

```python
a = 12

not a > 15
True
```

In this example we've modified the code we were previously using to add a midlife crisis detection for anyone between the ages of 45 and 55 using the "and" operator. They get to ride for free!
```python

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
# Here is the and condition we've created for the midlife crisis age range.
  elif age >= 45 and age <= 55:
    bill = 0
    print(f"You're having a midlife crisis. Your tickets are ${bill}. Good Luck!")  
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
   #Add $3 to bill
   bill += 3
 
  print(f"Your final bill is {bill}")
   
else:
  print("Sorry, you have to grow taller before you can ride.")
```

---

***Day 3 Challenge*** - [Code](https://github.com/TroyCaywood/Python/blob/main/100%20Days%20of%20Code/CodeChallenges/Day_3_Treasure_hunt.py)
