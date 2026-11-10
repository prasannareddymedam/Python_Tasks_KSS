#  Create a Number Guessing Game where: 
# The program generates a random number between 1 and 50 using random. 
# The user has 5 attempts to guess the number. 
# After each guess, calculate the absolute difference using math.fabs() and display how far the guess is from the correct number.

import random as r
import math as m

secret = r.randint(1,50)

for i in range(3):
    guess = int(input("Guess:"))

    if guess == secret:
        print("You Won!")
        break
    print ("Difference:", m.fabs(secret-guess))
    if guess <secret:
        print("Too Low")
    else:
        print("Too High")
else:
    print("You Lost! Number was:",secret)
