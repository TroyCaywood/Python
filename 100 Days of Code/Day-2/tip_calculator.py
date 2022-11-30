#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.\n")
bill_total = input("How much was your total bill?\n")
people = input("How many people are splitting the bill?\n")
percent = input("What percentage tip would you like to give?")

amount_paid = ((float(bill_total) / float(people)) * (float(percent) / 100 ) + float(bill_total))
total = "{:.2f}".format(amount_paid)


print(f"Each person should pay ${total}")
