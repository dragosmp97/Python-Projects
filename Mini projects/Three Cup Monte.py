import random

mylist = [" ", "0", " "]

def shuffle_list(mylist):
	random.shuffle(mylist)
	return(mylist)

mixedup_list = shuffle_list(mylist)

def player_guess():
	guess = " "
	while guess not in ["0","1","2"]:
		guess = input("Pick a number 0, 1 or 2: ")
	return int(guess)

guess = player_guess()

def check_guess(shuffle_list, player_guess):
	if mylist[guess] == "0":
		print("Correct!")
	else:
		print("Wrong guess!")
		print(mylist)

check_guess(mixedup_list, guess)