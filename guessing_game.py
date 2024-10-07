import random
global chances
import time

global hs_t 
hs_t = 99999999
   
def startup():
  global chances
  print("Welcome to the Guessing Game! \nI'm thinking of a number between 1 and 100.")
  print()
  print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
  print()
  diff_level = int(input("Enter your choice:"))
  if diff_level == 1:
    chances = 10
    print("Great! You have selected the Easy level. You have 10 chances to guess the number.")
    print("Let's start the game!")
  elif diff_level == 2:
    chances = 5
    print("Great! You have selected the Medium level. You have 5 chances to guess the number.")
    print("Let's start the game!")
  elif diff_level == 3:
    chances = 3
    print("Great! You have selected the Hard level. You have 3 chances to guess the number.")
    print("Let's start the game!")
  gamestart()

  
def gamestart():
  numguess = random.randint(1,100)
  
  timestart = time.time()
  global chances
  global hs_t
  global hs_a
  for i in range(chances):
    guess = int(input("Enter your guess:"))
    if guess == numguess:
      timeend = time.time()
      elapse_time = timeend - timestart
      round(elapse_time, 2)
      print("Congratulations! You guessed the correct", i ,"attempts!")
      print("You guess in" , round(elapse_time, 2) , "seconds" )
      if elapse_time < hs_t:
        hs_t = elapse_time
        print("New High Score!")
        break
      break
    else: 
      chances -= 1
      if guess > numguess:
        print("Your guess is too high.\n")
      if guess < numguess:
        print ("Your guess is too low.\n")
      continue
  print("Game Over!\n")
  try_again_menu()
  
def try_again_menu():
  print("Current High Score:", round(hs_t, 2), "seconds")
  print("Would you like to try again?")
  print("1. Yes")
  print("2. No")
  try_again = int(input("Enter your choice:"))
  if try_again == 1:
    startup()
  else:
    print("Thank you for playing!")
    exit()


startup()

