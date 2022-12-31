# Day 25 - Working with CSV File and the Pandas Library

## CSV
- A CSV is a file that stores
- Python has a built-in library for working with CSV files called CSV
- When you use `csv.reader()` it reads the CSV file and saves it as an object.
```python
import csv

with open("./weather_data.csv", mode="r") as weather_data:
    data = csv.reader(weather_data)
    print(data)
    # <_csv.reader object at 0x102959d20>
```
- We can treat it as a list and loop through the data:
```python
import csv

with open("./weather_data.csv", mode="r") as weather_data:
    data = csv.reader(weather_data)
    print(data)

    for row in data:
        print(row)
        # Would print:
            # ['day', 'temp', 'condition']
            # ['Monday', '12', 'Sunny']
            # ['Tuesday', '14', 'Rain']
            # ['Wednesday', '15', 'Rain']
            # ['Thursday', '14', 'Cloudy']
            # ['Friday', '21', 'Sunny']
            # ['Saturday', '22', 'Sunny']
            # ['Sunday', '24', 'Sunny']
```
- Now let's pull out just the temperatures and put them in their own list.
```python
import csv

with open("./weather_data.csv", mode="r") as weather_data:
    data = csv.reader(weather_data)
    print(data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)
    # This prints:
        # [12, 14, 15, 14, 21, 22, 24]
```
## Pandas!
- The built-in CSV library works fine, but a better library for dealing with datasets exists and that is: [Pandas](https://pandas.pydata.org)
- With panda doing our previous task is much simpler!
- All we have to do is `import pandas` and then `pandas.read_csv("filename")` and then we can tell it to print the column want.
```python
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

# This would print:
    # 0    12
    # 1    14
    # 2    15
    # 3    14
    # 4    21
    # 5    22
    # 6    24
    # Name: temp, dtype: int64`
```

- Pandas data is stored in either Dataframes or Series.
- A dataframe is basically the equivalent of a whole table or spreadsheet
- A series is the equivalent to a list or a single column in your table/spreadsheet
- You can do all sorts of things with Pandas. Such as converting your table to a dictionary.
```python
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
       
data_dict = data.to_dict()
print(data_dict)
# This would print:
    # {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
    # 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain',
    # 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}
```
- Or we could convert our temp series to a list
```python
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
# This would print:
    # [12, 14, 15, 14, 21, 22, 24]
```
- Pandas has a lot of useful methods. For example, we could find the average temp from our data by doing `print(data["temp"].mean())`
- Or we could find the max temperature with `print(data["temp"].max())`
- Instead of using the `[]` and the series name you can also just do `print(data.temp)` and get the same results with pandas since pandas converts each column name into attributes
- Make sure you are typing your series names EXACTLY how they appear in the dataframe. If the series has an uppercase letter, you need to use an uppercase letter when calling it.

## Working with Rows
- If you want to get the values from a specific row, you have to call a value in that row you're looking for by the series name
- For example, if we wanted to get all the values in the row where the day is Monday:
```python
print(data[data.day == "Monday"])
# This would print:
    #       day  temp condition
    # 0  Monday    12     Sunny
```
- If you wanted the whole row from whatever day has the max temp you could do:
```python
print(data[data.temp == data.temp.max()])
# This would print:
    # 6  Sunday    24     Sunny
```
- You can also save a row to a variable and then perform the same actions on it:
```python
monday = data[data.day == "Monday"]
print(monday.condition)

# This would print:
    # 0    Sunny
```
## Creating a DataFrame from Scratch
- You can also create a new dataframe from data in your code using `pandas.DataFrame()`
```python
import pandas

data_dict = {
    "Students": ["Amy", "James", "Angela"],
    "Scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
# This would print:
    #   Students  Scores
    # 0      Amy      76
    # 1    James      56
    # 2   Angela      65
```
- If you wanted to save your new dataframe to a csv file you could use `data.to_csv("new_csv.csv")` to save your dataframe to a CSV file in your current working directory

## Day 25 [Code Challenge](https://github.com/TroyCaywood/Python/tree/main/100%20Days%20of%20Code/CodeChallenges/Day-25) - U.S. States Game - Do not click before attempting yourself!