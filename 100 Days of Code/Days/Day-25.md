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