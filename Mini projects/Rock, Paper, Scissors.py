import random

while True:
    choices = ["ROCK","PAPER","SCISSORS"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, paper or scissors?: ").upper()

    if player == computer:
        print("\nYou chose: ", player)
        print("The computer chose: ", computer)
        print("\nIT'S A TIE!")
    elif player == "ROCK":
        if computer == "PAPER":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nPaper covers rock. YOU LOSE!")
        if computer == "SCISSORS":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nRock smashes scissors. YOU WIN!")
    elif player == "PAPER":
        if computer == "ROCK":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nPaper covers rock. YOU WIN!")
        if computer == "SCISSORS":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nScissors cuts paper. YOU LOSE!")
    elif player == "SCISSORS":
        if computer == "PAPER":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nScissors cuts paper. YOU WIN!")
        if computer == "ROCK":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nRock smashes scissors. YOU LOSE!")

    play_again = input("\nDo you want to play again? (YES/NO): ").upper()

    if play_again != "YES":
        break
print("\nOkay, bye then!")

