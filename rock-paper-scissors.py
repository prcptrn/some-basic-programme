from random import randint

rps_value = 0
player_move = True

while player_move:
    player_move = False
    rps = str(input("choose rock, paper or scissors: "))
    if rps == "rock":
        rps_value = 1
    elif rps == "paper":
        rps_value = 2
    elif rps == "scissors":
        rps_value = 3
    else:
        player_move = True

computer_rps = randint(1, 3)

if computer_rps == 1:
    print("computer chose rock")
    if rps_value == 1:
        score = "tied"
    elif rps_value == 2:
        score = "won"
    elif rps_value == 3:
        score = "lost"

elif computer_rps == 2:
    print("computer chose paper")
    if rps_value == 1:
        score = "lost"
    elif rps_value == 2:
        score = "tied"
    elif rps_value == 3:
        score = "won"

elif computer_rps == 3:
    print("computer chose scissors")
    if rps_value == 1:
        score = "won"
    elif rps_value == 2:
        score = "lost"
    elif rps_value == 3:
        score = "tied"

print("You have " + score)
