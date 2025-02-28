#Guessing game

import random

guesses = 5
secretNumber = random.randint(1,20)

name = input("Welcome to the guessing game! What is your name?")
print("Hi",name)
while guesses > 0:
    guess = input("Please input your guess between 1-20.")
    if guess.isalpha() or int(guess) > 20 or int(guess) < 1:
        print("Invalid input please try again")    
    elif int(guess) == secretNumber:
        took = int(guesses)
        guesses = -1
    else:
        guesses -= 1
        if int(guess) < secretNumber:
            print("Incorrect guess, It was too Low. You have",guesses,"guess/es remaining.")
        else:
            print("Incorrect guess, it was too High. You have",guesses,"guess/es remaining.")

if guesses == -1:
     print("Congratulations :D! You have guessed the correct number, with",took-1,"guess/es remaining.")
else:
    print("You have ran out of guesses :( Maybe you'll get it next time.")



        
