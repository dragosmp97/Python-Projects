# ------------------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    questions_num = 1

    for i in questions:
        print("------------------------------------")
        print(i)
        for j in options[questions_num-1]:
            print(j)
        choices = ["A", "B", "C", "D"]
        guess = input("\nEnter A, B, C or D: ").upper()
        if guess in choices:
            guesses.append(guess)
        while guess not in choices:
            guess = input("Please enter a valid answer: ").upper()
            if guess in choices:
                guesses.append(guess)
            continue

        correct_guesses += check_answer(questions.get(i),guess)
        questions_num += 1

    display_score(correct_guesses,guesses)
# ------------------------------------
def check_answer(answer,guess):

    if answer == guess:
        print("\nCORRECT!")
        return 1
    else:
        print("\nWRONG!")
        return 0
# ------------------------------------
def display_score(correct_guesses, guesses):
    print("------------------------------------")
    print("Results:")
    print("------------------------------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ",end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")
# ------------------------------------
def play_again():

    response = ""
    while response != "NO" and response != "YES":
        response = input("\nDo you want to play again? (YES/NO): ").upper()
        if response == "NO":
            return False
        elif response == "YES":
            return True
    if response == "NO":
        return False

# ------------------------------------

questions = {
    "What year was Python created?: ":"A",
    "Who created Python?: ":"B",
    "The name of python programming language is a tribute to which comedy group?: ":"C",
}

options = [["\nA. 1991", "B. 2006", "C. 2008", "D. 1997"],
           ["\nA. Bill Gates", "B. Guido van Rossum", "C. Bjarne Stroustrup", "D. Stephen Hawking"],
           ["\nA. Snake Island", "B. Lazy Python", "C. Monty Python", "D. Smosh"]]

new_game()

while play_again():
    new_game()

print("\nOkay, bye!")
