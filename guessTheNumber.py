#This is a guess the number game 

import random
secretNumer = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

# Ask the player to guess 6 times
print('rule #: You can only guess 6 times')
for guessTaken in range(1 ,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumer:
        print('Your guess is too low.')
    elif guess > secretNumer:
        print('Your guess is too high')
    else:
        break # This condition is the correct guess!

if guess == secretNumer:
    print('Good job! You passed my number in ' + str(secretNumer) + ' guesses!')
else:
    print('Nope. The number I was thinking if was ' + str(secretNumer))