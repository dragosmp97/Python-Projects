import random

rounds = 1
wins = 0
loses = 0
ties = 0

while True:
    choices = ["ROCK","PAPER","SCISSORS"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("\nRock, paper or scissors?: ").upper()

    if player == computer:
        print("\nYou chose: ", player)
        print("The computer chose: ", computer)
        print("\nIT'S A TIE!")
        ties += 1
    elif player == "ROCK":
        if computer == "PAPER":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nPaper covers rock. YOU LOSE!")
            loses += 1
        if computer == "SCISSORS":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nRock smashes scissors. YOU WIN!")
            wins += 1
    elif player == "PAPER":
        if computer == "ROCK":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nPaper covers rock. YOU WIN!")
            wins += 1
        if computer == "SCISSORS":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nScissors cuts paper. YOU LOSE!")
            loses += 1
    elif player == "SCISSORS":
        if computer == "PAPER":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nScissors cuts paper. YOU WIN!")
            wins += 1
        if computer == "ROCK":
            print("\nYou chose: ", player)
            print("The computer chose: ", computer)
            print("\nRock smashes scissors. YOU LOSE!")
            loses += 1

    play_again = ""
    while play_again != "NO" and play_again !="YES":
        play_again = input("\nDo you want to play again? (YES/NO): ").upper()
        if play_again == "NO":
            print("\nOkay, bye!")
            print("\nRounds played:", rounds)
            print("Wins:", wins)
            print("Loses:", loses)
            print("Ties:", ties)
            break
        elif play_again == "YES":
            continue
    if play_again == "NO":
        break

    rounds = rounds + 1
    print("\nRound:", rounds)
