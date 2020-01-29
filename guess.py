import random
n = 5
guess = int(input("Enter an integer from 1 to 99: "))
while n != "guess":
    print
    if guess < n:
        print ("guess is wrong")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print ("guess is wrong")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("you guessed it!")
        break
    print
