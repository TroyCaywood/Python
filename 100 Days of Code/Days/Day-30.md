# Day 30 - Errors, Exceptions and JSON DATA: Improving the Password Manager Program

## Catching exceptions

- In python, you can catch exceptions in your code using four keywords:
    + try:
      + Something that might cause an exception
    + except:
      + Do this if there **was** an exception. When creating an exception it's important to specify what type of exception such as FileNotFoundError
    + else:
      + Do this if there were no exceptions (no problems)
    + finally
      + Do this no matter what happens. Even if something fails or succeeded.

```python
#FileNotfound
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["not exist"])
    
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

# Get the error message and print it in the print command 
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

# If try block was successful
else:
    content = file.read()
    print(content)

# Runs no matter what    
finally:
    file.close()
    print("File was closed.")
```

## Raising your own Exceptions

- To create your own exceptions you use `raise:`
- Let's use raise to catch exceptions when someone enters unrealistic values for BMI calculation
```python
height = float(input("Height: "))
weight = float(input("Weight: "))

bmi = weight / height ** 2
print(bmi)

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
```

- Here is an example of error handling that will prompt the user to enter letters if they keep entering numbers
```python
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

def generate_word():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_word()
    else:
        print(output_list)


generate_word()
```
