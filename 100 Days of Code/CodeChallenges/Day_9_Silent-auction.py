from replit import clear
from art import logo
print(logo)

# Create empty dictionary
bids = {}
# Create bidding_finished variable to check if bidding is finished
bidding_finished = False

# Create highest bidder function with bidding_record parameter
def find_highest_bidder(bidding_record):
  # Set highest bid variable to 0 for comparision
  highest_bid = 0
  # Set winner variable to blank string
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  # for loop that loops through dictionary
  for bidder in bidding_record:
    # Create bid_amount variable that is equal to the value of the current bidder key
    bid_amount = bidding_record[bidder]
    # Test if the current key value is higher than the highest_bid variable
    if bid_amount > highest_bid: 
      # if it is higher set the highest_bid variable to the current bidder key value
      highest_bid = bid_amount
      # also set the winner variable to the current bidder key
      winner = bidder
  # Print the winner and bid aount
  print(f"The winner is {winner} with a bid of ${highest_bid}")

# Loop to get input
while not bidding_finished:
  name = input("What is your name?: ")
  # Converting price to integer is important for the find_highest_bidder function
  price = int(input("What is your bid?: $"))
  # Add name key with price value to bids dictionary EX "Troy", 99
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    # Exit loop by setting bidding_finished to True when user types "no"
    bidding_finished = True
    # Call find_highest bidder function to find the highest bidder
    find_highest_bidder(bids)
  elif should_continue == "yes":
    # Clear the screen so the next user can't see the previous user's bid amount
    clear()
  
