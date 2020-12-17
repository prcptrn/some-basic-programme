def problem():
    if sign == '+':
        add()
    elif sign == '-':
        sub()
    elif sign == '*':
        multi()
    elif sign == '/':
        div()
    else:
        print('please select the correct sign')


def add():
    print(float(a) + float(b))


def sub():
    print(float(a) - float(b))


def multi():
    print(float(a) * float(b))


def div():
    print(float(a) / float(b))


nie_sign = 1
nie_a = 1
nie_b = 1

while nie_a == 1:
    nie_a = 0
    try:
        a = float(input("a: "))
    except ValueError:
        print("this isn't a number")
        nie_a = 1

while nie_b == 1:
    nie_b = 0
    try:
        b = float(input("b: "))
    except ValueError:
        print("this isn't a number")
        nie_b = 1

while nie_sign == 1:
    nie_sign = 0
    sign = str(input('choose sign: '))
    if sign == "+":
        add()
    elif sign == "-":
        sub()
    elif sign == "*":
        multi()
    elif sign == "/":
        if b != 0:
            div()
        else:
            print("Don't divide by 0!")
            print("please choose correct sign")
            nie_sign = 1
    else:
        print("please choose correct sign")
        nie_sign = 1
