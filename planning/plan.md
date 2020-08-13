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
- User can see the number of cards in the session (default is all cards)
- User can choose a smaller subset of cards
- ...by entering a number between 1 and 5 in the command line
- ...e.g. user types 5: session cards will be 1x1 through 5x5 (25 cards)
- For each card, user sees the "front" of the card (question)
- User can provide an answer and is then shown the "back" of the card (answer)
- For each card, keeps track of how many times users have answered correctly and incorrectly
- User can create new cards by providing two numbers and an answer
- Model for Card (id Number, series Number, question String, answer String or Number, correct Number, incorrect Number)
- id: 1 through 36 (37+ if users add cards)
- series: 6 (this is the 6x1, 6x2,...6x n series)
- question: '6x2'
- answer: '12' or 12
- correct: 3
- incorrect: 1

### Silver: looks and works better

- Increase number of flash cards (1x1 through 12x12)
- When user creates a card, checks that the answer is valid before saving in the dbase

### Gold: bells and whistles

- User can login and retrieve flash cards from previous sessions
- For each card, keeps track of how many times a specific user has answered correctly and incorrectly
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

- On load, a welcome message and directions display in the command line
- Prompt: how many flashcards
