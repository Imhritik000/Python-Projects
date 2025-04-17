                                            #Number guessing game

"""GOAL : The computer randomly picks a numer between 1 to 100 .
the user has to guess it - and the program gives hint like 'TOO HIGH' or 'TOO LOW'
until the user get it right"""



import random

number_to_guess = random.randint(1,100)
guess = None
attempts = 0


print("Welcome to number guessing game!")
print("I am thinking a number between 1 to 100")

while guess!=number_to_guess:
    guess = int(input("Enter your guess here :"))
    attempts += 1

    if guess < number_to_guess:
        print("too low! try again")

    elif guess > number_to_guess:
        print("too high! try again")

    else :
        print(f"Congratulations! you guessed right it in {attempts} tries.")