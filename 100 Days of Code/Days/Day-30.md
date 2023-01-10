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
## Upgrading the Password Manager
- To make our data easier to work with we are going to change the format from a plain text file to [JSON](https://en.wikipedia.org/wiki/JSON)
- A JSON is basically composed of a bunch of nested lists and dictionaries and uses a key value pair data structure
```python
import json

# Write
json.dump()
# Read
json.load()
# Update
json.update()
```
- Let's update our `save_password()` function to save into a json file
```python
import json

def save_password():
    email = email_user_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    # Create nested dictionary for json file.
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showinfo(title="Empty Fields", message="Please don't leave any empty fields!")

    else:
        # Create json file if it doesn't exist
        with open("./data.json", mode="w") as data_file:
            # Write to JSON file using the data_file dictionary and indent 4 spaces to make it easier for humans to read
            json.dump(new_data, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
```
- Now our `data.json` looks like this
```json
{
    "https://www.gmail.com": {
        "email": "test@gmail.com",
        "password": "s37O!DLRNpgK*7#p"
    }
}
```
- When using `json.load()` to read JSON data, the data is converted to a regular python dictionary
- The only problem with what we're doing now, is that if we change it to append mode it will just append on another nested dictionary and it won't be valid anymore
- What we need to do is user `json.load()` to convert the data to a dictionary and then append it to the dictionary and convert it back to JSON
```python
    else:
        with open("./data.json", mode="r") as data_file:
            # Reading old data
            data = json.load(data_file)
            # Updating old data with new data
            data.update(new_data)
        with open("./data.json", mode="w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)
            
            website_entry.delete(0, END)
            password_entry.delete(0, END)
```
- Now new entries save correctly
```json
{
    "https://www.gmail.com": {
        "email": "test@gmail.com",
        "password": "s37O!DLRNpgK*7#p"
    },
    "https://www.gamespot.com": {
        "email": "test@gmail.com",
        "password": "$*%3#3k7zUU1QawHUx"
    }
}
```
## Add Error Handling

- Lets add some error catching to catch if there is no json file so the program doesn't error out
```python
    else:
        try:
            with open("./data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        # If no json file create it        
        except FileNotFoundError:
            with open("./data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            
            with open("./data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

```

## Add Search Function
- Now we'll add a search function so we can look up passwords through the program
```python
def search():
    website = website_entry.get()
    try:
        with open("./data.json", mode="r") as data_file:
            # Convert to dictionary
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="No Data", message="No datafile found. Please create at least one entry.")
    else:
        # Look for website key in data
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            # Display found username and password
            messagebox.showinfo(title=website_entry.get(), message=f"Username: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Doesn't Exist",
                                message=f"Sorry, {website_entry.get()} doesn't exist in the database")

```
- Now we'll assign that to a new search button next to the website field
```python
search_button = Button(text="Search", width=13, command=search)
search_button.grid(column=2, row=1)
```

- We could have technically handled the website not being found with an exception, but it's better to do things with if/else if we can and leave exceptions for things that probably won't happen often
- Only use exception handling when you don't have an easy alternative

## Day 30 [Code Challenge](https://github.com/TroyCaywood/Python/tree/main/100%20Days%20of%20Code/CodeChallenges/Day-30) - No challenge today, but here is the final code for the password manager