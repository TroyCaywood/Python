## Day 3 - Conditional Statements, Logical Operators, Code Blocks and Scope

---

<p align=center><b>Conditional Statements</b></p>

**If/Else Statements**
- An If/Else statement runs a block of code if a statement is True, if the statement is False it runs the else block of code.

In this example, it would print "continue" since the water level is less than 80 and therefore the if statement is true. Notice the indentation on the print lines. This is important in python and tells the computer that it needs to run that line when the if or else statement is met.
```python
water_level = 50
if water_level > 80:
  print("Drain water")
else:
  print("continue")
```
