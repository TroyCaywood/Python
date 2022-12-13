import random
from art import logo
from replit import clear

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  def calculate_score(cards):
    total = sum(cards)
    if total == 21:
      total = 0
  
  
   
    for card in cards:
      if card == 11 and total > 21:
        cards.remove(card)
        cards.append(1)
        total = sum(cards)
       
    return total
    
  should_continue = True
  computer_score = calculate_score(computer_cards)
  user_score = calculate_score(user_cards)
  print(f"Your cards are {user_cards} your score is {user_score}")
  print(f"Computer cards are {computer_cards} computer's score is {computer_score}")
  
  while should_continue:
    if computer_score == 0:
      print("Computer wins with 21. Blackjack!")
      should_continue = False
    if user_score == 0:
      print("User wins with 21. Blackjack!")
      should_continue = False
    elif user_score > 21:
      print(f"Player busts with {user_score}. GAME OVER!")
      should_continue = False
    else:
      draw_again = input(f"Your score is currently {user_score}. Would you like to draw another card? Y or N: ")
      if draw_again.lower() == "y":
        draw = deal_card()
        user_score += draw
        print(f"You drew {draw}")
      elif draw_again.lower() == "n":
        should_continue = False
  while computer_score != 0 and computer_score <= 17:
    computer_score += deal_card()
  
  def compare(user_score, computer_score):
    if user_score == computer_score:
      return("It's a tie!!")
    elif computer_score == 0 or computer_score == 21:
      return("Computer has BlackJack. Computer wins!")
    elif user_score == 0 or user_score == 21:
      return("Player has BlackJack. Player Wins!")
    elif user_score > 21:
      return("Player went over 21. Computer wins!")
    elif computer_score > 21:
      return("Computer went over 21. Player wins!")
    elif user_score > computer_score:
      return("You win!")
    else:
      return("You Lose!")

  print(f"Computer Score: {computer_score}\n  Player Score: {user_score}\n {compare(user_score, computer_score)}")

play_game()

while input("Would you like to play again? Y or N: ").lower() == "y":
  clear()
  play_game()

