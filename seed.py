from model import *

greatestFactor = 6
cards = []
index = 0

# Create card variable names
for i in range(0, greatestFactor*greatestFactor+1):
	cards.append(f'card{i}')

# Seed dbase with cards model
# for i in range(1, greatestFactor+1):
# 	for j in range(1, greatestFactor+1):
# 		index+= 1
# 		cards[index] = Card(series=i, question=f"{i} x {j}", answer=i*j, correct=0, incorrect=0)
# 		cards[index].save()