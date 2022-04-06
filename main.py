import random
import os
from art import logo


EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5


def take_a_random_number():
	numbers = []
	for number in range(1, 101):
		numbers.append(number)

	random_number = random.choice(numbers)
	return random_number


def incorrect_answer(text, type):
	if type == str:
		while True:
			check_string = input(text).lower()
			if check_string == 'easy' or check_string == 'hard':
				return check_string
			else:
				print('Incorrect answer!')
	else:
		while True:
			try:
				check_string = int(input(text))
			except ValueError:
				print('Incorrect answer!')
			else:
				return check_string
				


def choose_difficulty():
	answer = incorrect_answer("Choose a difficulty. Type 'easy' or 'hard': ", str)

	if answer == 'easy':
		return EASY_DIFFICULTY
	else:
		return HARD_DIFFICULTY


def compare_answer(number, correct_number):
	end_game = True

	if number > correct_number:
		return 'Too high.'
	elif number < correct_number:
		return 'Too low.'
	else:
		return end_game


def number_guessing_game():
	print(logo)
	print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
	number = take_a_random_number()
	tries = choose_difficulty()

	while tries != 0:
		print(f'You have {tries} attempts remaining to guess number.')
		user_number = incorrect_answer("Make a guess: ", int)
		result = compare_answer(user_number, number)

		if result == True:
			print(f'You are right! It is really {number}')
			break
		else:
			print(result)

		print('Guess again.')
		print('-' * 60)
		tries -= 1

	if tries == 0:
		print(f'You lose! Correct number was {number}!')



os.system('cls' if os.name == 'nt' else 'clear')
number_guessing_game()
