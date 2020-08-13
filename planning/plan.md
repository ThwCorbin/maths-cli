# Maths-CLI Planning

## Brief

A Python command line application for mathematics flash cards.

## Bronze, Silver, and Gold

### Requirements all

- Python, SQL database, PeeWee models
- Working seed script for the database (creating database and tables)
- README is well documented

### Bronze: minimum viable product

- User can practice multiplication tables with flash cards (1x1 through 6x6)
- User can provide a name, which will be used as the Session instance
- User can see the number of cards in the session (36 cards)
- Or user can choose a smaller subset of cards
- ...by entering a number between 1 and 5 in the command line
- ...e.g. user types 5: session cards will be 1x1 through 5x5 (25 cards)
- User can see the number of cards user picked for the session
- For each card, user sees the "front" of the card question
- User can provide answer and is then shown the "back" of the card answer
- For each card, keeps track of how many times a user has answered correctly and incorrectly in the session
- User can create new cards
- ...by entering a number between 7 and 9
- ...e.g. user types 7, which will add 7x1 through 7x7 to the Session instance
- Model for Session (card_id Number, card_line Number, card_name String, card_answer String or Number, correct Number, incorrect Number)
- card_id: 1 through 36 (higher if user adds cards)
- card_line: 6 (this is the 6 x n line)
- card_name: '6x2'
- card_answer: '12' or 12
- correct: 3
- incorrect: 1

### Silver: looks and works better

- User can practice multiplication tables with flash cards (1x1 through 12x12)
- User can add 13, 14, and/or 15 lines (e.g. 15x12)

### Gold: bells and whistles

- User can login and retrieve flash cards from previous sessions
- Update and delete cards
- User can select just the multiples of one number (8x1, 8x2, 8x3...8xN)
- User can get division, addition, and subtraction cards
- User interface built with tkinter, pygame, or PySimpleGUI

## Data

- SQL
- PostgreSQL
- PeeWee

## Pseudocode

### Bronze
