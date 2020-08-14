from model import *

def get_cards(num_cards):
	all_cards = Card.select().where(Card.id < int(num_cards) + 1)
	for card in all_cards:
		print(card.question)

def begin_session():
	num_cards = input(f'How many flash cards? Enter number between 1 and 36: ')
	print(f'Retrieving {num_cards} flash cards')
	get_cards(num_cards)

def main():
	# welcome_msg = 'Welcome to Maths-CLI. This is a flash card project to help you practice multiplication.'
	# set_up ='Set up: Install dependencies in the Pipfile with pipenv. Then enter "pipenv shell" in the terminal to create a virtual environment.'
	# create_dbase = 'Create Database: Now open a separate terminal window enter "psql". At the =# prommpt, enter "CREATE DATABASE maths;"'
	# seed_dbase = 'Seed Database: Back in the virtual environment terminal, enter "python3 seed.py"'
	# print(welcome_msg)
	# print(set_up)
	# print(create_dbase)
	# print(seed_dbase)
	begin_session()

main()