import random
from hidden_words import word_list
from hangman_stages import stages


def test(chosen_word,hidden_word):
  print(chosen_word)
  print(hidden_word)

def guess_letter():
  guess = input("Guess a letter: ")
  while not guess.isalpha():
    guess = input("Please enter a letter: ")
  return guess.lower()

def hidden_init(chosen_word):
  h = []
  for i in range(len(chosen_word)):
    h.append('_')
  return h

def update_hidden_word(chosen_word, hidden_word, guess):
  for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
      hidden_word[i] = guess
  return hidden_word

def display_hidden_word(hidden_word):
  display = ""
  for l in hidden_word:
    display += l
  print(display)
  
def play():
  attempts = 0
  chosen_word = random.choice(word_list)
  hidden_word = hidden_init(chosen_word)
  
  # main core loop of game
  while attempts < 6 and '_' in hidden_word:
    print(stages[attempts])
    guess = guess_letter()
    if guess in chosen_word:
      print("guessed correctly")
      hidden_word = update_hidden_word(chosen_word, hidden_word,guess)
      display_hidden_word(hidden_word)
    else:
      attempts += 1
      attempts_left = 6 - attempts
      print(f"You have {attempts_left} attempts left")
      display_hidden_word(hidden_word)
  if attempts == 6 and '_' in hidden_word:
    print(stages[attempts])
    print("Loser")
  else:
    print("Winner")

play()