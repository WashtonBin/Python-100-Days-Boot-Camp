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

def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1, 101)
  
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    attempts = 10
  elif difficulty == "hard":
    attempts = 5
  
  def check_number(number, guess):
    if number > guess:
      print("Too low.")
    elif number < guess:
      print("Too high.")
    else:
      print(f"You got it! The answer was {number}.")
  
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    check_number(number, guess)
    if number == guess:
      attempts -= 0
      break
    else:
      attempts -= 1
  
  if attempts == 0:
    print("You've run out of guesses, you lose.")
    print(f"Pssst, the correct answer is {number}")

play_game()
