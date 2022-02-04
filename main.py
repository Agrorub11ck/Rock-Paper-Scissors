import random


def stats(names):
	new_file = open('rating.txt', 'r', encoding='utf-8')
	stat_list = new_file.readlines()

	for elem in stat_list:
		if names in elem:
			new_list = elem.split()
			break
	else:
		new_list = [names, 0]
	new_file.close()

	return new_list


def win_lose(player, comp):
	if len(option) == 3:
		if player == 'rock' and comp == 'scissors' or player == 'scissor' and comp == 'paper' or player == 'paper' and comp == 'rock':
			return True
	elif abs((option.index(player) - (len(option) // 2)) % (len(option)) - 1)  < option.index(comp):
		return True
	return False


name = input('Enter your name: ')
print('Hello,', name)
stat_list = stats(name)
option = input().split(',')
if len(option) == 1:
	option = ['rock', 'scissors', 'paper']

print("Okay, let's start")

while True:
	move = input()
	if move == '!rating':
		print('Your rating:', stat_list[1])
		continue

	computer_move = random.choice(option)
	if move == '!exit':
		print('Bye!')
		break
	elif move == computer_move:
		print(f'There is a draw ({move})')
		stat_list[1] = int(stat_list[1]) + 50
	elif move not in option:
		print('Invalid input')
	elif win_lose(move, computer_move):
		print(f'Well done. The computer chose {computer_move} and failed')
		stat_list[1] = int(stat_list[1]) + 100
	else:
		print(f'Sorry, but the computer chose {computer_move}')
