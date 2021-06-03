# Guessing Game with 3 tries
print("Welcome to the guessing game...\nYou will have 3 tries to guess the correct number...\nLets begin...")
roll = randint(1,6)
i = 0
while i < 3:
  user_Guess = int(input("Guess a number bewteen 1 and 10; Or press 999 to quit << "))

  if user_Guess == 999:
    print("Thank you for playing!")
    break

  if user_Guess == roll:
    print("Well done!")
    break
  else:
    i += 1
    if i == 3:
      print("Sorry out of guesses")
      break
    print("Nope, try again << ")
  
print("Goodbye!")
