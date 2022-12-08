rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

player_choice = int(input("Choose rock paper or scissors. Type 0 for Rock, 1 for Paper, 2 for Scissors"))

if player_choice < 0 or player_choice >= 3:
  print("Invalid Choice. Try again.")
else:
  cpu_choice = random.randint(0, 2)

  game = [rock, paper, scissors]

  print(game[player_choice])
  print(f"CPU Chooses {game[cpu_choice]}!")
  
  if player_choice == cpu_choice:
    print("It's a tie! Play again!")
  elif cpu_choice > player_choice:
    print("Computer Wins!")
  elif player_choice > cpu_choice:
    print("You Win!")
  elif player_choice == 0 and cpu_choice == 2:
    print("You Win!")
  elif cpu_choice == 0 and player_choice == 2:
    print("Computer Wins!")
  elif player_choice > 3:
    print("You typed an invalid number. Play again.")
