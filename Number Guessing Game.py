import random

print('\nNumber Guessing Game\n___________________________________\n')
print('I am thinking of a number between 1 and 100')

secret = random.randint(1, 100)
tries = 0

while True:
    guess = int(input('Your guess: '))
    tries = tries + 1

    if guess < secret:
        print('Too low!')
    elif guess > secret:
        print('Too high!')
    else:
        print('\n___________________________________\n\nCorrect! You found it in', tries, 'tries\n')
        break