nie = True
even = True

while nie:
    nie = False
    try:
        number = float(input("choose number:"))
    except ValueError:
        print("This isn't a number")
        nie = True

something = float(number / 2)

if float(something) != int(something):
    even = False
else:
    even = True

if even:
    print(str(number) + " is even")
elif not even:
    print(str(number) + " isn't even")

if even:
    something = float(number / 4)
    if float(something) != int(something):
        div_four = False
    else:
        div_four = True

if div_four:
    print("also, " + str(number) + " can be divided by 4")
