from random import randint
number = randint(0, 10)
nie = 1
chances = 3

print("Rules: \n You have 3 chances \n You must guess the drawn number \n Don't use decimal numbers")

while chances > 0:
    while nie == 1:
        nie = 0
        try:
            ch_number = int(input('Choose a number from 0 to 10: '))
            ch_number = int(ch_number)
            if ch_number > 10:
                print("Choose number that isn't greater than 10.")
                nie = 1
            elif ch_number < 0:
                print("Choose number that isn't smaller than 0.")
                nie = 1
        except ValueError:
            print('…')
            nie = 1

    if ch_number == number:
        print('You won')
        chances = -1
    elif ch_number > number:
        if chances == 1:
            chances = 0
        else:
            print('The drawn number is smaller')
            chances -= 1
            print('remaining chances: ' + str(chances))
    elif ch_number < number:
        if chances == 1:
            chances = 0
        else:
            print('The drawn number is greater')
            chances -= 1
            print('remaining chances: ' + str(chances))
    nie = 1

if chances == 0:
    print('You lost')

print('The drawn number was: ' + str(number))
