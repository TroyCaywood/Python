# Day 10 - Functions With Outputs

## More Functions

For functions with outputs, rather than giving the function any arguments, you leave between the parenthesis blank and return the result and this allows you to store the function in a variable later
```python
def my_function():
    result = 3 * 2
    return result

ouput = my_function()
```

Function for converting a name to title case:
```python
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    
    print(f"{formatted_f_name} {formatted_l_name}"

format_name("bOB", "cALiFornIA")


# This would print Bob California
```

If we used return rather than print, the output of f_name and l_name replace the formatted_name() part of the code in the final_name variable and the final_name variable becomes equal to Bob California or we could just print the format_name function with our arguements. Basically anything after the return in a function is what replaces where the function was called.
```python
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
 
final_name = format_name("bOB", "cALiFornIA")
print(final_name)
print(format_name("bOb", cALiFornIA"))

# Both print functions would print Bob California
```

## More about return statements

-You can have multiple return statements in a function, but when the function gets to a return the return is what tells the function to stop running

Now we are asking the user for their first name and last name and we added a line in our format name function that checks whether the user entered blank entry and if they did, the function exits.
```python
def format_name(f_name, l_name):
    if f_name == "" or l_name = ""
        return "You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
 
print(format_name(input("What is your first name?"), input("What is your last name"))

# Now if someone enters a blank name, the console would print "You didn't provide valid inputs"
```

## Docstrings

- A Python docstring is a string used to document a Python module, class, function or method, so programmers can understand what it does without having to read the details of the implementation. Also, it is a common practice to generate online (html) documentation automatically from docstrings. Docstrings are contained within three sets of quotation marks and are the first line after defining a function. Docstrings can be multiple lines without causing issues. Can also be used on its own without being in a function to create a multi-line comment. Though, python documentation recommends against doing this and the better way is to write your comments, highlight them and press ctlr+/ to comment all the lines

Our previous format_name function with a docstring that describes what it does
```python
def format_name(f_name, l_name):
"""Take a first and last name and format it so it is 
in title casing format"""
    if f_name == "" or l_name = ""
        return "You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
```

## Print versus Return
- Using return can be a better solution when you want to store the results of a function in a variable and user it in other areas of your code. If you simply printed instead of using result, you wouldn't be able to do so.

## Recursion
- Recursion is calling a function within itself. This could be useful if you wanted to start a function over from the beginning out of a loop for example. Be careful with recursion though since it's an easy way to get your code stuck in an infinite loop. Make sure you have a condition that needs to be met in order for the function to call itself.
