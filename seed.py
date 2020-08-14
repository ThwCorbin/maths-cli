from model import *

largestFactor = 6
cards = []
index = 0

for i in range(0, largestFactor*largestFactor+1):
	cards.append(f'card{i}')

for i in range(1, largestFactor+1):
	for j in range(1, largestFactor+1):
		index+= 1
		cards[index] = Card(series=i, question=f"{i} x {j}", answer=i*j, correct=0, incorrect=0)
		cards[index].save()