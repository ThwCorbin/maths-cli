# Maths-CLI Planning

## Brief

A Python command line application for mathematics flash cards.

## Bronze, Silver, and Gold

### Requirements all

- Python, SQL database, PeeWee models
- Working seed script for the database (creating database and tables)
- README is well documented

### Bronze: minimum viable product

- User can practice multiplication tables with flash cards (1x12 through 12x12)
- User can provide a name, which will be used as the Session instance
- User can see the number of cards in the session (144 cards)
- Or user can choose a smaller subset of cards
- ...by entering a number between 1 and 12 in the command line
- ...e.g. user types 5: session cards will be 1x12 through 5x12 (60 cards)
- User can see the number of cards user picked for the session
- For each card, user sees the "front" of the card question
- User can provide answer and is then shown the "back" of the card answer
- Keeps track of how many times a card has been answered correctly and incorrectly in the session
- User can create new cards
- ...by entering a number between 13 and 15
- ...e.g. user types 13, which will add 13x1 through 13x13 to the Session instance
- Model for Session (card_id Number, card_name String, card_answer String or Number, correct Number, incorrect Number)
- card_id: 1 through 144
- card_name: '8x8'
- card_answer: '64' or 64
- correct: 3
- incorrect: 1

### Silver: looks and works better

- User can login and retrieve flash cards from previous sessions
- Update and delete cards
- Model for User (user_name String, user_password String, session_ids Array of Numbers)

### Gold: bells and whistles

- User can select just the multiples of one number (8x1, 8x2, 8x3...8xN)
- User can get division, addition, and subtraction cards
- User interface built with tkinter, pygame, or PySimpleGUI

## Data

- SQL
- PostgreSQL
- PeeWee

## Pseudocode

### Bronze

- On load, a welcome message and directions display in the command line
- Prompt: how many flashcards

* Prompt: type name to begin session
* Check dbase for name, ask user to provide password ("password" for all users)
* New user types a name to start a session set up
* Each session has an id, which is saved in the user instance
* A session instance stores the user_name and the session_cards used in that session. Each card User provides number of flashcards they want to review. First flashcard displays (e.g. “8 x 8").
