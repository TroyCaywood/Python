#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

# Create random number global variable
RAND_NUMBER = random.randint(1, 100)


# Define difficulty function. If easy, guesses = 10 and return 10, if hard guesses = 5 and return 5.
def difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard.': ")
    if difficulty.lower() == "easy":
        guesses = 10
        return guesses
    elif difficulty.lower() == "hard":
        guesses = 5
        return guesses

# Define start game function
def start_game():
    # Condition variable for while loop
    playing = True
    print(logo)
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.\n")
    # Remain guesses variable that calls the difficulty function to obtain the number of guesses for the game.
    remain_guesses = difficulty()
    
    # Start of while loop.
    while playing:
        # Prompt for a guess
        player_guess = int(input(f"Make a guess you have {remain_guesses} guesses: "))
        # If statements to check guess
        if remain_guesses == 1:
            print(f"You're out of guesses. The number was {RAND_NUMBER}")
            playing = False
        if player_guess < RAND_NUMBER:
            print("Too low")
            remain_guesses -= 1
            print(f"You have {remain_guesses} guesses left.")
        elif player_guess > RAND_NUMBER:
            print("Too High")
            remain_guesses -= 1
            print(f"You have {remain_guesses} guesses left.")   
        elif player_guess == RAND_NUMBER:
            print(f"You guessed the correct number. {RAND_NUMBER}")
            playing = False

# Call start game function
start_game()
    
