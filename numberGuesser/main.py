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

def welcome():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100.")

def getDifficulty():
  """Returns the validated number of guesses based on the difficulty"""
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  while difficulty not in ["easy", "hard"]:
    print("Invalid input")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  return difficulty

def getGuess(attempts):
  """Returns validated guess"""
  print(f"You have {attempts} attempts remaining to guess the number.")
  while True:
    try:
      guess = int(input("Make a guess: "))
      break
    except ValueError:
      print("Invalid input. Plese enter a number.")
  return guess

def hint(userGuess, target):
  """Displays 'too high' or 'too low' depending on guess"""
  if userGuess > target:
    print("Too high.")
  else:
    print("Too low.")
    
def guess():
  EASY = 10
  HARD = 5
  TARGET = random.randint(1,100)
  userCorrect = False
  
  welcome()
  DIFFICULTY = getDifficulty()
  attempts = EASY if DIFFICULTY == "easy" else HARD

  while attempts > 0 and not userCorrect:
    user_guess = getGuess(attempts)
    userCorrect = user_guess == TARGET
    hint(user_guess, TARGET)
    if(not userCorrect):
      attempts -= 1

  if userCorrect:
    print(f"You got it! The answer was {TARGET}.")
  else:
    print(f"You've run out of guesses, you lose. The answer was {TARGET}.")
guess()
