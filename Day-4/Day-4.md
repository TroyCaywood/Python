## Day Four - Randomisation and Python Lists

---
**Modules**
- A module is a file containing a set of functions you want to include in your application.
- For example, you could create a file called my_module.py containing this code:
```python
pi = 3.14159246
```
- To use the module, you would just have to add import my_module to the code you are writing. You could do things like:
```python
print(my_module.pi)
```

**Randomization**

- Python has a [module](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences) available for generating randomness called "random"
- You must import the module before being able to use it

This code example will generate a random number between 1 and 10 every time random_integer is called.
```python
import random

random_integer = random.randint(1, 10)
print(random_integer)
```
- You can also generate a random float using random.random(), however it will only give you a float between 0 and 1 (**NOT** including 1)
- If you wanted to generate a float that was larger than 1, you can multiply random.random() by the ending integer. 0 to 5 in this example.
```python
import random

randomFloat = random.random() * 5

print(randomFloat)
```
You could use this to do something like make a random heads or tail generator
```python
import random

coin = random.randint(0, 1)

if coin == 1:
    print("Heads")
else:
    print("Tails")
```

---

**Lists**
-
