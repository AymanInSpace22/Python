from random import random

side = ("Head", "tail")
prefix = ("Well done", "Oh dear")
score = 0
for n in range(3):
  computer = (random() > 0.5)
  user = int(input("0 for Head and 1 for Tail: "))
  print("You guessed", side[user],"and the computer tossed", side[computer])
  score += user == computer
print(prefix[score == 0], "- you had", score, "correct guess"+"es"*(score != 1) + "!")
