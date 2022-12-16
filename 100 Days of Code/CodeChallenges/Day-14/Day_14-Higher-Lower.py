import random
from art import logo
from game_data import data
from replit import clear

CHOICE_LIST = []
CHOICE = CHOICE_LIST.append(random.choice(data))

for i in range(2):
    CHOICE_LIST.append(random.choice(data))
    while CHOICE_LIST[0]['name'] == CHOICE_LIST[1]['name']:
        CHOICE_LIST.pop(0)
        CHOICE_LIST.append(random.choice(data))

print(CHOICE_LIST)


def play_game():
    points = 0
    still_playing = True
    is_correct = ""
    while still_playing:
        print(logo)
        if is_correct == "correct":
          print(f"You're right! You have {points} points.")
          is_correct = ""
        print(
            f"{CHOICE_LIST[0]['name']} a {CHOICE_LIST[0]['description']} from {CHOICE_LIST[0]['country']}\n"
        )
        print("versus\n")
        print(
            f"{CHOICE_LIST[1]['name']} a {CHOICE_LIST[1]['description']} from {CHOICE_LIST[1]['country']}\n"
        )

        player_choice = input("Who has more followers? Type A or B:\n")
        if player_choice.lower() == "a":
            if CHOICE_LIST[0]["follower_count"] > CHOICE_LIST[1][
                    "follower_count"]:
                points += 1
                is_correct = "correct"
                CHOICE_LIST.pop(1)
                CHOICE_LIST.append(random.choice(data))
                while CHOICE_LIST[0]['name'] == CHOICE_LIST[1]['name']:
                    CHOICE_LIST.pop(1)
                    CHOICE_LIST.append(random.choice(data))
                clear()

            else:
                print(
                    f"Sorry, that's incorrect. {CHOICE_LIST[0]['name']} had {CHOICE_LIST[0]['follower_count']} million followers and {CHOICE_LIST[1]['name']} had {CHOICE_LIST[1]['follower_count']} million followers.\nYou had {points} points. You lose!"
                )
                still_playing = False
        if player_choice.lower() == "b":
            if CHOICE_LIST[1]["follower_count"] > CHOICE_LIST[0][
                    "follower_count"]:
                points += 1
                is_correct = "correct"
                CHOICE_LIST.pop(0)
                CHOICE_LIST.append(random.choice(data))
                while CHOICE_LIST[0]['name'] == CHOICE_LIST[1]['name']:
                    CHOICE_LIST.pop(0)
                    CHOICE_LIST.append(random.choice(data))
                clear()

            else:
                print(
                    f"Sorry, that's incorrect. {CHOICE_LIST[1]['name']} had {CHOICE_LIST[1]['follower_count']} million followers and {CHOICE_LIST[0]['name']} had {CHOICE_LIST[0]['follower_count']} million followers.\nYou had {points} points. You lose!"
                )
                still_playing = False


play_game()
