# Import modules
import random
from art import logo
from replit import clear

# Define play_game function
def play_game():
  print(logo)
  # Create blank cards lists to user and computer
  user_cards = []
  computer_cards = []

  # Create deal_card function that contains a card list and then chooses a random card from         the list and returns that card
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

  # For integer in range of 2 append two random cards to user_cards list and computer_cards         list
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  # Define calculate_score function that totals a list of cards and if that total is equal to       21, it sets the total to 0. Also checks if card is equal to 1 and the total is greater         than 21. If the total is greater than 21 it removes the 11 card and appends a card equal       to 1 and then changes the total to the new sum and returns the total. 
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

  # Define should_continue condition for while loop
  # Define computer_score and user_score as the sum of all items in the cards lists
  # Print current scores and cards for computer/user
  should_continue = True
  computer_score = sum(computer_cards)
  user_score = sum(user_cards)
  print(f"Your cards are: {user_cards}\nYour score is: {user_score}\n")
  print(f"Computer cards are: {computer_cards}\nComputer's score is: {computer_score}\n")

  # Start of while list. Check if computer or user have a blackjack or if the user has gone         over 21.
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
    # Ask the player if the ywould like to draw again
    else:
      draw_again = input(f"Your score is currently {user_score}. Would you like to draw another card? Y or N: ")
      # If player wants to draw again, create draw_user variable that calls deal_card function         to get a random card. Append the random card to the user_cards list and then set               user_score to the new sum of user_cards list. Print card the user drew.
      if draw_again.lower() == "y":
        draw_user = deal_card()
        user_cards.append(draw_user)
        user_score = sum(user_cards)
        print(f"You drew {draw_user}\n\n")
      # If player doesn't want to draw again, set should_continue to False to exit loop
      elif draw_again.lower() == "n":
        should_continue = False

  # While loop for computer to draw cards. While computer doesn't have a blackjack and their      score is under 17 the computer will draw random cards and then add the computer_cards         list then change the computer score to the new sum. 
  while computer_score != 0 and computer_score <= 17:
    computer_cards.append(deal_card())
    computer_score = sum(computer_cards)
  # Create compare function to find the winner
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

  # Print the final scores
  print(f"Computer Score: {computer_score}\nComputer Hand {computer_cards}\n\nPlayer Score: {user_score}\nPlayer Hand: {user_cards}\n\n{compare(user_score, computer_score)}")
# Start the game by calling play_game function
play_game()

# While loop for ending game
while input("Would you like to play again? Y or N: ").lower() == "y":
  clear()
  play_game()

