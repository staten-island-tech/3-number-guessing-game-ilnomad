import random

random_number = random.random()
print(random_number)

def countdown():
    number=input("countdown from ")
    number=int(number)
    print(number)
    while number<0 or number>1:
        if number>1:
            number=number-1
            print(number)
        elif number<1:
            number=number+1
            print(number)
        else:
            print("0")
def numberguess2():


    guesshistory=[]
    x=int(input("Min? "))
    y=int(input("Max? "))
    n=random.randint(x,y)
    i=0
    m=0
    while not n==m:
        m=int(input("Guess a number "))
        if n>m:
            print("Your number is smaller than the random one ")
            guesshistory.append(m)
            i=i+1
            print(guesshistory)
        elif m>n:
            print("Your number is greater than the random one ")
            guesshistory.append(m)
            i=i+1
            print(guesshistory)
        else:
            print("You won 10 won money thingy currencie thing ")
            for i in range(i-1):
                print(guesshistory[i])

