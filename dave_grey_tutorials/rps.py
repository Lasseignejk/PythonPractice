import sys
import random


player_score = 0
computer_score = 0
num_ties = 0

def handle_win(winner, score):
	score += 1
	if winner == 'player':
		print("You win!")
	elif winner == 'computer': 
		print("Python wins!")
	else: 
		print("Tie game!")
	return score



should_stop = False
while should_stop == False:

	player_choice = input("Enter ...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n")
	if player_choice == 'q': 
		sys.exit("Thanks for playing!")
	player = int(player_choice)
	if player < 1 or player > 3: 
		sys.exit("You must enter 1, 2, or 3.")

	computer_choice = random.choice([1,2,3])



	print("")

	print("You chose " + player_choice + ".")
	print("Python chose " + str(computer_choice) + ".")

	if player == 1 and computer_choice == 3: 
		player_score = handle_win('player', player_score)
	elif player == 2 and computer_choice == 1: 
		player_score = handle_win('player', player_score)
	elif player == 3 and computer_choice == 2: 
		player_score = handle_win('player', player_score)
	elif player == computer_choice: 
		num_ties = handle_win('tie', num_ties)
	else: 
		computer_score = handle_win('computer', computer_score)
	
	print("")
	print("You: " + str(player_score))
	print("Computer: " + str(computer_score))
	print("Ties: " + str(num_ties))
	should_continue = input("Do you want to play again? Y/N\n")
	if should_continue.lower() == 'y':
		print("")
		continue
	else: 
		sys.exit("Thanks for playing!")
	