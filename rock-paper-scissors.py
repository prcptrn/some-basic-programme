from random import choice


def check(playera):
    global rps
    global usr
    for el in rps:
        if playera == el['name']:
            usr = el
            return True
    return False


player_move = True
r = {'name': 'rock', 'win': ['scissors']}
p = {'name': 'paper', 'win': ['rock']}
s = {'name': 'scissors', 'win': ['paper']}
rps = [r, p, s]

while player_move:
    player_move = False
    player = input("chose rock, paper or scissors: ")
    if not check(player):
        print("not ok")
        player_move = True

computer = choice(rps)

if computer['name'] == player:
    print('computer has chosen ' + computer['name'])
    print('The result is draw')
elif computer['name'] in usr['win']:
    print('computer has chosen ' + computer['name'])
    print("You won")
else:
    print('computer has chosen ' + computer['name'])
    print("You lost")
