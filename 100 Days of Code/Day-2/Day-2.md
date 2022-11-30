## Day Two - Data Types and Manipulating Strings

---

<p align = center><b>Data Types</b></p>

**Strings**
- Strings are a set of characters surrounded by quotation marks.

```python
"Hello, this is a string."
```
**Subscripting**
- Selecting a character in a string using [] with the number of the character in the string. The first character in a string is always 0. Don't forget, a space in a string counts as a character.

```python
print("Hello"[0])
```
Would print the H character since it is the first character in the string.
```
H
```
```python
print("Hello"[4])
```
Would print o since it is the fourth character in the string.
```
o
```
- "12345" would still be treated as a string rather than a number. Anything surrounded by quotes is a string.

**Integer**
- A set of whole numbers not surrounded by quotations. 12345 is an integer "12345" is not.

- To make large numbers easier to read, you can put an underscore between integers and the computer will still treat it as one number. 123_456_789 is the same as 123456789.

**Float**
- A set of numbers with a decimal point (the decimal point can "float" to any place in a number). 123.456 for example

**Boolean**
- A data type with only two possible values. True or False. The first character is always capitalized on True or False. Used to evaluate if an expression is True or False.

---

**Type Errors**
- Strings and integers cannot be added together.
```python
num_char = len(input("What is your name?"))
print("Your name has " + num_char + " characters.")
```
This code would return a type error since len is counting the number of charcters in the name and returning an integer and then you're trying to combine an integer with a string.
- If you aren't sure what datatype your function is outputting you can use the type() function to check.
```python
num_char = len(input("What is your name?"))

print(type(num_char))
```
Pretend you entered your name when prompted. The computer would then store the number of charcters in your name in the num_char variable as an integer. Type would return:
```
<class 'int'>
```
- To fix the previous example, we need to convert the integer into a string using str()
```python
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
```
Pretend we entered the name Troy. The code will now count the number of characters as 4 and then convert it to the string "4" and store it in the new_num_char variable.
```
Your name has 4 characters.
```
- Other datatypes can be converted as well.
- float() is used to convert whole numbers into floats.

---

**Mathematical Operations**
- You can perform mathematical operations on integers in python ( strings can be "added" together using +)
- "+" for addition  4 + 3
- "-" for subtraction 4 - 3
- "*" for multiplication 4 * 3
- "/" for division 4 / 3 
  + Note: in division the numbers returned are always returned as a float rather than an integer.
- "**" for exponents (to the power of) 4 ** 3
- When working with mathematical expressions in python, remember PEMDAS (**P**lease **E**xcuse **M**y **D**ear **A**unt **S**ally) for the order of operations
  + **P**arentheses
  + **E**xponents
  + **M**ultiplication
  + **D**ivision
  + **A**ddition
  + **S**ubtraction
- When you have multiplication and division in the same calculation, they are of equal importance but whichever is furthest to the left is executed first. Same for addition and subtraction in the same calculation.
- To round an calculation use the round function. round(2.66666, 2) the second number is the number of places that you want to round to. This example would round to 2.67.
- If you want a division equation to round to the nearest whole number use floor division by using two "//"  8 // 3 would round to 2.
- When a number or equation is stored in a variable, you can modify the stored equation or number easily using variable += 1 in this case it would add one to the stored variable.
```python
score = 4
score += 1
print(score)
```
When score is printed, it would now be 5
```
5
````
 - Other mathematical operations can be performed on a variable the same way. "-=" "*=" "/=" etc.

---

- An F-string is used if you want to combine strings with other datatypes such as integers or floats without having to convert each type to a string first. This is accomplished by putting an f before the string and then putting the variables in {} within the string. EX:

```python
score = 0
height = 1.8
isWinning = True

#f-string
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
```
This would print
```
Your score is 0, your height is 1.8, you are winning is True
```
