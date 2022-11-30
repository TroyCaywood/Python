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
