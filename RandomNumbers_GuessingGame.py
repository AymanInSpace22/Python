from random import randint
# the randit function works with whole numbers
# the randit() function takes 2 arguments
die = randint(1,6)
print(die)

# tuple: remember its 0-based, this meand the "Ryder" starts at 0 and "Saber" is actually the 3rd position
name = ("Ryder", "Caster", "Saber", "Lancer", "Berzeker", "Assassin", "Archer")
# we are using lenth - 1 rather than a hard-coded position so we can freely update our list rather than having to update the number everytime we add or subtract from the list
print(name[randint(0, len(name)-1)])


from random import random 
# the random() function works with floating point #'s bewtween 0-1
# furthermore, the random() function taked no arguments 
print(random())


# if you want your random #'s to lean more towards higher or lower then you can square root them then add or subtract 1
die = int((random()**10)*6+1)
print(die)


print()



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



'''
# a simpler guessing game with unlimited tries
roll = randint(1,6)
flag = True
while flag:
  user_Guess = int(input("Guess a number bewteen 1 and 10; Or press 999 to quit << "))

  if user_Guess == 999:
    print("Thank you for playing!")
    flag = False
    break

  if user_Guess == roll:
    print("Well done!")
    flag = False
  else:
    print("Nope, try again << ")
    flag
'''
