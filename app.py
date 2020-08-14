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
	welcome_msg = 'Welcome to Maths-CLI. This is a flash card project to help you practice multiplication.'
	print(welcome_msg)
	begin_session()
main()