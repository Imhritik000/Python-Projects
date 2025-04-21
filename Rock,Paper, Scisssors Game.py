                                    #Let's Play ROCK,PAPER,SCISSORS


"""GOAL : Prepare a game in which User selects rock, paper, or scissors 
        — computer randomly picks — and then compare who wins, Make it simple and user friendly"""


import random

Choices = ["rock", "paper" ,"scissors"]
print("ROCK,PAPER,SCISSORS GAME ✊✋✌️ ")

while True:
    user =input("Choose ROCK,PAPER OR SCISSORS (OR 'quit' to stop):") .lower()
    if user == 'quit':
        print("thanks for playing!")
        break

    if user not in Choices :
        print("invalid choice , try again !")
        continue

    computer = random.choice(Choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
            (user == "paper" and computer == "rock") or \
            (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")