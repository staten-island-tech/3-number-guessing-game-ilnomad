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
    x=input("Minimum?")
    y=input("Maximum?")
    x=int(x)
    y=int(y)
    random.randint(x,y)

numberguess()