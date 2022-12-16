import random
from art import logo
from game_data import data
from replit import clear


CHOICE_LIST = []
CHOICE = CHOICE_LIST.append(random.choice(data))

for i in range(2):
  CHOICE_LIST.append(random.choice(data))

print(CHOICE_LIST)



def play_game():
  points = 0
  still_playing = True
  while still_playing:
    print(logo)
    print(f"Current Points: {points}\n")
    print(f"{CHOICE_LIST[0]['name']} a {CHOICE_LIST[0]['description']} from {CHOICE_LIST[0]['country']} {CHOICE_LIST[0]['follower_count']}\n" )
    print("versus\n")
    print(f"{CHOICE_LIST[1]['name']} a {CHOICE_LIST[1]['description']} from {CHOICE_LIST[1]['country']} {CHOICE_LIST[1]['follower_count']}\n" )
    
    
    player_choice = input("Who has more followers? Type A or B:\n")
    if player_choice.lower() == "a":
      if CHOICE_LIST[0]["follower_count"] > CHOICE_LIST[1]["follower_count"]:
        print(f"You're right {CHOICE_LIST[0]['name']} has {CHOICE_LIST[0]['follower_count']} followers. {CHOICE_LIST[1]['name']} only has {CHOICE_LIST[1]['follower_count']} followers")
        points += 1
        print(f"You have {points} points!")
        CHOICE_LIST.pop(1)
        CHOICE_LIST.append(random.choice(data))
        #print(CHOICE_LIST)
        
       
      else:
        print(f"Sorry, that's incorrect. You had {points} points. You lose!")
        still_playing = False
    if player_choice.lower() == "b":
      if CHOICE_LIST[1]["follower_count"] > CHOICE_LIST[0]["follower_count"]:
        print(f"You're right {CHOICE_LIST[1]['name']} has {CHOICE_LIST[1]['follower_count']} followers. {CHOICE_LIST[0]['name']} only has {CHOICE_LIST[0]['follower_count']} followers")
        points += 1
        print(f"You have {points} points!")
        CHOICE_LIST.pop(0)
        CHOICE_LIST.append(random.choice(data))
        #print(CHOICE_LIST)
      
      else:
        print(f"Sorry, that's incorrect. You had {points} points. You lose!")
        still_playing = False

play_game()
