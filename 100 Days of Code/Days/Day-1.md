# Day One - Strings, Input, and Variables

---

## Strings


- To print text to console.
```python
print("Hello world!")
```
```
Hello World!
```
- Plain text is called a string in programming. Text within print parenthesis **must** be in quotation marks or single quotes. Best practice to use double quotes, but use single quotes if there are more quotes in the string EX: 
```python
 print("This is how you print things print('Hello world!'). Isn't that neat?")
 ```
 ```
 This is how you print things print('Hello world!'). Isn't that neat?
 ```
- \n within a string prints anything after the \n to a new line
```python
print("Hello World!\nHello World!")
```
```
Hello World!
Hello World!
```
- Strings can be concatenated (combined) using the + sign

```python
print("Hello World!" + " It's me!")
```
```
Hello World! It's me!
```

- **Syntax highlighting** is color coding for different parts of code in an IDE. Can be useful when troubleshooting errors (IE string is white instead of red, missing quotation marks)

---

## Input



- To prompt a user for input use the input() function.
```python
input("What is your name?")
```
- In this example, the user would be prompted with "What is your name?" and then the program will wait for them to type something and press enter. The typed text is then passed on to the input function and stored.
- You can also put an input function inside of a print function to print the result
```python
print("Hello " + input("What is your name?") + "!")
```
- If the user typed in Bob the result would be
```
Hello Bob!
```
- The length of a string can be found using len()

---

## Variables

- A Python variable is a symbolic name that is a reference or pointer to an object. Once an object is assigned to a variable, you can refer to the object by that name. But the data itself is still contained within the object.

```python
name = "Troy"
print(name)
```
```
Troy
```
- A variable can be changed later in your code. It will not always hold the same value
```python
name = "Troy"
print(name)

name = "Bob"
print(name)
```
```
Troy
Bob
```
- Variables can be named almost anything you want, but make sure they are easily understandable later. Avoid using ambiguous variable names. 
- You **cannot** have space in variable name, but underscores are ok. EX:
```python
best_pie = "pumpkin"
```
- Numbers can be in the variable name, but they **cannot** be the first character in the variable name. 
- It is best practice not to use privledged names of functions such such as print or input for variable names.
- Pay attention to your variable names when referencing them in functions etc. Spelling or casing errors will genearate a NameError if the variable is not defined by that spelling or casing.

---

## Day 1 Project[Code Challenge](https://replit.com/@TroyCaywood/band-name-generator-start?v=1) - [Code](https://github.com/TroyCaywood/Python/blob/main/100%20Days%20of%20Code/CodeChallenges/Day_1_band_generator.py) Do **NOT** click if you plan on doing the project yourself.
