#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# create password list to store random choices in
password_list = []

#Take choice int variable for letters and put it into for loop. The for loop goes from 1 to the chosen number + 1 (because otherwise it would not include the chosen number) then for each number in that range (1 through chosen number +1) the for loop uses the random module choice method to choose a random index in the letters list and then adds it to the password_list list.
for char in range(1, nr_letters + 1):
  password_list += random.choice(letters)

 #repeat for symbols list
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

  #repeat for numbers list
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

# Use the shuffle method from random module to randomly rearrange the password_list list to increase randomization of password.
random.shuffle(password_list)

# Create a variable called password set to a blank string where we can store the final password
password = ""

# Using a for loop, we now pull each index from the password_list and add it to the empty string to combine the list into one string.
for character in password_list:
  password += character

#Using and fstring print the final password.
print(f"Your randomly generated password is {password}")
