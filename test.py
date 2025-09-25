import random

random_number = random.random()
print(random_number)

def countdown():
    number=input("countdown from")
    number=int(number)
    print(number)
    while number <0 or number >1:
        if number > 1:
            number = number - 1
            print(number)
        elif number < 1:
            number = number + 1
            print(number)
        else:
            print("0")

def numberguess():
    x=0
    y=1
    x=int(x)
    y=int(y)
    t=False
    n=random.randint(x,y)
    while not t==True:
        x=input("Minimum?")
        y=input("Maximum?")
        m=input("Guess de number")
        if n == m:
            print("great job")
            t=True
        else:
            n=random.randint(x,y)
            print("guess again")
            numberguess
numberguess()