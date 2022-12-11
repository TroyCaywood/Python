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
To loop through a dictionary
```python
for key in dictionary:
    print(key)
    print(dictionary[key])
```
- If you only called print(key) all that would print would be the keys in the dictionary and not the value. 

Here is an example of using a for loop to create a new dictionary of student grades from another dictionary with their scores.
```python
# Dictionary of student scores
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# Create empty dictionary
student_grades = {}

# For loop to loop that populates the student_grades dictionary
for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    
print(student_grades)

# This would print: {'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}
```
## Nesting lists and dictionaries
- Lists and dictionaries can be nested inside of each other
```python
nested = {"Key1": {"dictionary2": "key2}, 
    "Key2": ["list_item1", "list_item2"]
}
```
Another example. We have a travel log dictionary that contains states as the keys and the values are lists that contain cities in those states:
```python
travel_log = {"Kansas": ["Kansas City", "Topeka", "Pratt"],
    "Oklahoma": ["Oklahoma City", "Alva", "Ponka City"],
    "California": ["San Francisco", "Los Angeles", "Palm Springs"]
}
```
You can also nest other dictionaries inside of dictionaries or other lists inside of lists (though nesting lists inside of each other isn't as useful.
In this example we nest 3 other dictionaries with the cities visited in a list in tha dictionary as well as the total visits to those cities.
```python
travel_log = "Kansas": {"cities_visited": ["Kansas City", "Topeka", "Pratt"], "Total Visits": 10},
    "Oklahoma": {"cities_visited": ["Oklahoma City", "Alva", "Ponka City"], "Total Visits": 9},
    "California": {"cities_visited": ["San Francisco", "Los Angeles", "Palm Springs"], "Total Visits: 6}
```
Nesting dictionaries in a list. To make things easier to read. It's best to separate each item in the list/dictionary so they are on their own line.
```python
travel_log =[ 
    {
        "State": "Kansas",
        "cities_visited": ["Kansas City", "Topeka", "Pratt"],
        "Total Visits": 10
    },
    {
        "State": "Oklahoma",
        "cities_visited": ["Oklahoma City", "Alva", "Ponka City"],
        "Total Visits": 9
    },
    {
        "State": "California",
        "cities_visited": ["San Francisco", "Los Angeles", "Palm Springs"],
        "Total Visits: 6
    }
]
```

Here is an example of creating a funciton to add a new dictionary to a list of dictionaries.

```python
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

# Define function and parameters
def add_new_country(country_visited, times_visited, cities_visited):
    # Create an empty dictionary
    new_country = {}
    # Add country name to new dictionary
    new_country["country"] = country_visited
    # Add times visited to new dictionary
    new_country["visits"] = times_visited
    # Add cities visited to new dictionary
    new_country["cities"] = cities_visited
    # Use the append function to append the new dictionary to the travel_log dictionary
    travel_log.append(new_country)

# Add a new country
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# This would print [{'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}, {'country': 'Germany', 'visits': 5, 'cities': ['Berlin', 'Hamburg', 'Stuttgart']}, {'country': 'Russia', 'visits': 2, 'cities': ['Moscow', 'Saint Petersburg']}]
```
