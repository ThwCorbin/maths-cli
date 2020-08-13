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
- For each card, user sees the "front" of the card (question)
- User can provide an answer and is then shown the "back" of the card (answer)
- For each card, keeps track of how many times users have answered correctly and incorrectly
- User can create new cards by providing two numbers and an answer
- Model for Card (id Number, series Number, question String, answer String or Number, correct Number, incorrect Number)
- id: 1 through n
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

1. User runs a command to start the app
2. Display welcome message with directions and prompt
3. Prompt: How many flash cards? (Select Enter for all or a number < x)
4. If user selects Enter, select all the flash cards from the dbase
5. Else if user submits a number, check that number is less than row count
6. If true, select x number of cards
7. Else if false, display message and prompt
8. Prompt: submit a number less than x or select enter for all cards
9. Repeat steps 4 - 8 until user submits valid number or selects enter
10. Display total flash cards number
11. Display first flashcard question, card number (Card 1 of x), and prompt
12. Prompt: submit a number to answer
13. User submits number
14. Check answer and update dbase for that card (correct or incorrect)
15. If correct, display correct message and prompt
16. Else if incorrect, display incorrect message and prompt
17. Prompt: Press return or spacebar for next question
18. Display next flashcard question, card number (Card 2 of x), and prompt
19. Repeat steps 12 - 18 until all cards have been answered
20. Display flash cards finished message and prompt
21. Prompt: Start another session, end, or add flash card
22. If start again, prompt step 3
23. Else if end, display thank you and goodbye message
24. Else if add, display message and prompt
25. Prompt: provide two numbers to multiply and an answer like this: 8, 9, 72
26. User submits three numbers separated by commas 8, 9, 72
27. Update database and display success message and prompt
28. Prompt: see steps 21 - 27
