import os

word = os.getenv("SECRET_WORD")
letter1 = os.getenv("letter1")
letter2 = os.getenv("letter2")
letter3 = os.getenv("letter3")
letter4 = os.getenv("letter4")
letter5 = os.getenv("letter5")
letter6 = os.getenv("letter6")
show_letter1 = "_"
show_letter2 = "_"
show_letter3 = "_"
show_letter4 = "_"
show_letter5 = "_"
show_letter6 = "_"

user = " "
#guesses_count = 3
guesses = 5
out_of_guesses = False
def intro():
  print("**WELCOME TO GUESS THE WORD**")
  print("In this game you have to guess the secret word.")
  print("You only get 5 guesses!")
  print("Lets start")
  print(" ")


intro()

while user.lower() != word and not (out_of_guesses):
  if 0 < guesses:
    guesses -= 1
    user = input("\nEnter word pls: ")
    if letter1 in user.lower():
      print("The secret word contains the letter: " + letter1)
      show_letter1 = letter1
    if letter2 in user.lower():
      print("The secret word contains the letter: " + letter2)
      show_letter2 = letter2
    if letter3 in user.lower():
      print("The secret word contains the letter: " + letter3)
      show_letter3 = letter3
    if letter4 in user.lower():
      print("The secret word contains the letter: " + letter4)
      show_letter4 = letter4
    if letter5 in user.lower():
      print("The secret word contains the letter: " + letter5)
      show_letter5 = letter5
    if letter6 in user.lower():
      print("The secret word contains the letter: " + letter6)
      show_letter6 = letter6
    print(show_letter1 + show_letter2 + show_letter3 + show_letter4 + show_letter5 + show_letter6)

  else:
    out_of_guesses = True

if out_of_guesses:
  print("\nYou out of guesses, try again!")
  print(":):):):):):):):)")
else:
  print("\nWel done!")
  print("You won with " + str(guesses) + " guesses over")