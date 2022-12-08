# Day 7 - Hangman

- Today we will be building a hangman game. This is a fun project and I would encourage you to do the project yourself before reading this page.

**Breaking down problems into flowcharts**

- Before starting a project, it's a good idea to break down your program into a flowchart.

For example we could flowchart our game of hangman like this:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/52113778/206577471-61f8eaf2-bbdb-4867-a89e-fe3cbde0baf8.png">

- First we need to build a way to select a random word from a list, break that word up into separate letters, prompt the user for input, and then compare that input to the selected random word.

```python
#Step 1 
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Choose a letter"\n).lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for word in chosen_word:
  if word == guess:
    print("Right")
  else:
    print("Wrong")
```

- Now we need to change our code so it displays blanks instead of the letters in the chosen word and then replaces those blanks with the player's guess if it's correct
``python
#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


guess = input("Guess a letter: ").lower()
display = []
word_length = len(chosen_word)

for letter in chosen_word:
  display += "_"

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(word_length):
  letter = chosen_word[position] 
  if letter == guess:
    display[position] = guess


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)
```
