# Day 9 - Beginner Dictionaries, Nesting and Secret Auction

## Dictionaries
- Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
- Dictionaries allow you to group together and tag related pieces of information.
- You can kind of think of dictionaries as table

| Key      | Value                                                                   |
|----------|-------------------------------------------------------------------------|
| Bug      | An error in a program that prevents a program from running as expected. |
| Function | A piece of code that you can Easily call over and over again.           |
| Loop     | The action of doing something Over and over again.                      |

- To create a dictionary, the format is {key: value}
Our table above would look like this as a dictionary
```python
Programming_Dictionary = {"Bug": "An error in a program that prevents a program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}
```
- To make your dictionaries more readable, best practices is to put a return after each dictionary entry and then indent the lines under the first line one indention and put the end curly bracket in line with the start of the dictionary.
- Accessing values in a dictionary is similar to accessing lists.
```python
Programming_Dictionary = {"Bug": "An error in a program that prevents a program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

print(Programming_Dictionary["Bug"]

# This would print "An error in a program that prevents a program from running as expected."
```
- If you mistype a key when calling a dictionary, you will get a Key Error
- When calling a dictionary key make sure you use the correct datatype. If you made the keys strings, use the string. If they were integers, use integers. You'll get an error otherwise.

To add a new item to a dictionary call the dictionary with the key you want to add and = and then the value of that key
```python
Programming_Dictionary["Cat"] = "A small furry animal."
```

To create an empty dictionary
```python
new_dictionary = {}
```

To clear an existing dictionary
```python
dictionary = {"Ham Sandwich": "Delicous",
    "Peanutbutter Sandwich": "Also delicious",
    "Vegemite sandwich": "Not sure"
}

dictionary = {}

print(dictionary)

# This would simply print {} since the told it the dictionary is empty now
```

To change an existing dictionary entry call the dictionary and the key you want to change and then type = and the new value
```python
dictionary["Vegemite sandwich"] = "Possibly delicious"
```
