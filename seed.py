from model import *

greatestFactor = 12
cards = []
index = 0

# Drop card table prior 
db.drop_tables([Card])

# Create card table
db.create_tables([Card])

# Create card variable names
for i in range(0, greatestFactor*greatestFactor+1):
	cards.append(f'card{i}')

# Seed dbase with cards model
for i in range(1, greatestFactor+1):
	for j in range(1, greatestFactor+1):
		index+= 1
		cards[index] = Card(series=i, question=f"{i} x {j}", answer=i*j, correct=0, incorrect=0)
		cards[index].save()