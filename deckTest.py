from cards import *

suites = ["hearts", "spades", "diamonds", "clubs"]
deck = deck([])

for suite in suites:
	a = []
	for name in range(2,15):
		if name == 11:
			name = "jack"
		if name == 12:
			name = "queen"
		if name == 13:
			name = "king"
		if name == 14:
			name = "ace"
		a.append(card(name,suite))
	deck + a
	
deck.shuffle()

for card in deck.cards:
	print card
	
'''
from cards import *

c1 = card(1, "a")
c2 = card(2, "b")

print c1 == c2

set2 = deck(range(1,100))
set2.shuffle()
'''