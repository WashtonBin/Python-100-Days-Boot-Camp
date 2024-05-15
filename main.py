#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
from replit import clear

#check number if it is correct or not and print the result
def check_number(number, guess, attempts):
  if number > guess:
    print("Too low.")
    return attempts - 1
  elif number < guess:
    print("Too high.")
    return attempts - 1
  else:
    print(f"You got it! The answer was {number}.")
    return -1

def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  #set guess number 1 - 100
  number = random.randint(1, 10)
  
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  #set difficulty level
  if difficulty == "easy":
    attempts = 10
  elif difficulty == "hard":
    attempts = 5
  else:
    print("Invalid input.")
    return
    
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = check_number(number, guess, attempts)
    # #if guess is wrong, reduce attempts by 1
    # #if guess is correct, end the game
    # if number == guess:
    #   attempts -= 0
    # else:
    #   attempts -= 1
  #if attempts is 0, end the game
  if attempts == 0:
    print("You've run out of guesses, you lose.")
    print(f"Pssst, the correct answer is {number}")
    return
  elif attempts == -1:
    return

play_game()
while input("Type 'y' to play again or 'n' to exit: ") == "y":
  clear()
  play_game()

print("Good Bye")