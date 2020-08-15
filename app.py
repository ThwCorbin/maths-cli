import random
from model import *

total_cards = Card.select().count()
print(total_cards)

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

			      The database already has questions
			      for numbers 1 through 12. Consider
			       adding a flashcard with the first
			           number greater than 12.

			              Example: 13, 3, 39

			---------------------------------------------
	'''
	add_card_value = input(add_card_msg)
	new_card_arr = add_card_value.replace(" ", "").split(",")

	series = int(new_card_arr[0])
	question = f"{new_card_arr[0]} x {new_card_arr[1]}"
	answer = new_card_arr[2]
	new_card = Card(series=series, question=question, answer=answer)
	new_card.save()
	
	add_confirm_msg = f'''
			---------------------------------------------
			           We added your flashcard
			              to our database!

			              Question: {question}
			              Answer:   {answer}

			              Lets start your
			           next practice session.
			---------------------------------------------
	'''
	print(add_confirm_msg)
	begin_session()
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
		if user_add_card == "y":
			add_card()
		else:
			begin_session()
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
		
		if user_answer == card.answer:
			correct+= 1
			correct_msg = f'''
			---------------------------------------------
			
			         Correct! {card.answer} is the answer.
			'''
			print(correct_msg)
		else:
			incorrect+= 1
			incorrect_msg = f'''
			---------------------------------------------

			         Incorrect. The answer is: {card.answer}
			'''
			print(incorrect_msg)
		status_msg = f'''
			---------------------------------------------
			               Correct:   {correct}
			               Incorrect: {incorrect}
			               Remaining: {remaining_cards}
			---------------------------------------------
			'''
		print(status_msg)
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
		invalid_msg = f'''
			---------------------------------------------
			        There are {total_cards} flash cards.
			       Please provide a valid number.
			---------------------------------------------
		'''
		print(invalid_msg)
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
	retrieving_msg = f'''
			---------------------------------------------
			      Retrieving {num_cards} flash cards
			---------------------------------------------
	'''
	print(retrieving_msg)
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