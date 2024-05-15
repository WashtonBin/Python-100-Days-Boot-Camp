from art import logo, vs 
from game_data import data
from replit import clear
import random 

def get_random_account():
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer (a_followers, b_followers):
  if a_followers > b_followers:
    return "a"
  else:
    return "b"

def play_game():
  score = 0
  # a and b_data are list of dictionary
  a_data = get_random_account()
  # a and b are value of dictionary
  a = format_data(a_data)
  b_data = get_random_account()
  b = format_data(b_data)
  print(logo)
 
  while True:
    if score > 0:
      clear()
      print(logo)
      print(f"You're right! Current score: {score}")
    print(f"Compare A: {a}")
    print(vs)
    print(f"Against B: {b}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # get a and b's follower_count'
    a_follower_count = a_data["follower_count"]
    b_follower_count = b_data["follower_count"]
    is_correct = check_answer(a_follower_count, b_follower_count)
    # if user_guess is correct, game continues and b instead of a
    # and then create a new b and b_data
    if is_correct == user_guess:
      score += 1
      
      a = b
      a_data = b_data
      b_data = get_random_account()
      b = format_data(b_data)
    
    
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      break



play_game()
#restart the game if the user needs
while input("Do you want to play again? Type 'Y' or 'N': ").capitalize() == "Y":
  clear()
  play_game()

print("Good Bye")