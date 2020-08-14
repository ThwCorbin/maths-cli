import random
from model import *
from seed import greatestFactor

total_cards = greatestFactor ** 2

def goodbye():
	goodbye_msg = f'''
			---------------------------------------------
			          We hope you learned a lot 
			         about multiplication today!
				   
			                  Goodbye!

			---------------------------------------------
	'''
	print(goodbye_msg)

def add_card():
	add_card_msg = f'''
			---------------------------------------------
			      Enter two numbers to multiply and
			      their product separated by commas.

			              Example: 8, 9, 72

			---------------------------------------------
	'''
	add_card_value = input(add_card_msg)
	print(add_card_value)

#/add_card()

def user_choices():
	user_choices_msg = f'''
			---------------------------------------------
			       Would you like another session? 
			             Enter "y" or "n"

			---------------------------------------------
	'''
	user_add_card_msg = f'''
			---------------------------------------------
			    Would you like to create a flash card? 
			             Enter "y" or "n"

			---------------------------------------------
	'''

	user_choice = input(user_choices_msg)

	if user_choice == "y":
		user_add_card = input(user_add_card_msg)
		add_card()
	else:
		goodbye()
#/user_choices()

def session_finished(correct, num_flash_cards):
	end_session_msg = f'''
			---------------------------------------------
			             Session complete!

			    You answered {correct} flash cards correctly
			          out of {num_flash_cards} flash cards
	
			---------------------------------------------
	'''
	print(end_session_msg)
	user_choices()
#/session_finished()

def show_card(cards_shuffled):
	correct = 0
	incorrect = 0
	num_flash_cards = len(cards_shuffled) 
	
	for card in cards_shuffled:
		remaining_cards = num_flash_cards - (cards_shuffled.index(card)+1)

		user_answer = input(f'''
			    What is the product of {card.question}? 
			---------------------------------------------
			''')
		
		# user_answer and card.answer are strings
		if user_answer == card.answer:
			card.correct+= 1
			correct+= 1
			# print('---------------------------')
			print(f'''
			---------------------------------------------
			
			         Correct! {card.answer} is the answer.
			''')
		else:
			card.incorrect+= 1
			incorrect+= 1
			print(f'''
			---------------------------------------------

			         Incorrect. The answer is: {card.answer}
			''')
		print(f'''
			---------------------------------------------
			               Correct:   {correct}
			               Incorrect: {incorrect}
			               Remaining: {remaining_cards}
			---------------------------------------------
			''')
	session_finished(correct, num_flash_cards)
#/show_card()

def shuffle(cards_session):
	random.shuffle(cards_session)
	show_card(cards_session)
#/shuffle()

def get_cards(num_cards):
	if num_cards == '' or num_cards == ' ':
		get_cards(total_cards)
	elif int(num_cards) > total_cards:
		print(f'There are {total_cards} flash cards. Please provide a valid number.')
		begin_session()
	else:
		cards_session = [];
		all_cards = Card.select().where(Card.id < int(num_cards) + 1)
		for card in all_cards:
			cards_session.append(card)
		shuffle(cards_session)
#/get_cards()

def begin_session():
	num_cards = input(f'''
			       How many flash cards would you 
			       like for this practice session? 
			       Enter a number between 1 and {total_cards}
			---------------------------------------------
			                      
	''')
	print(f'''
			---------------------------------------------
			      Retrieving {num_cards} flash cards
			---------------------------------------------
	''')
	get_cards(num_cards)
#/begin_session()

def main():
	welcome_msg = f'''
			---------------------------------------------
			            Welcome to Maths-CLI!

			        This app provides flash cards
			     to help you practice multiplication
	
			---------------------------------------------
	'''
	print(welcome_msg)
	begin_session()
#/main()

main()