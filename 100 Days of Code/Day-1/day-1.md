## Day One

---

<p align=center><b>Strings</b></p>


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

<p align=center><b>Input</b></p>



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
