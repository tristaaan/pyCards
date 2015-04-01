from cards import *

suites = ["hearts", "spades", "diamonds", "clubs"]
set = deck([])

for y in suites:
	a = []
	for x in range(2,15):
		if x is 11:
			x = "jack"
		if x is 12:
			x = "queen"
		if x is 13:
			x = "king"
		if x is 14:
			x = "ace"
		a.append(card(x,y))
	set + a
	
set.shuffle()

for x in set.cards:
	print x
	
'''
from cards import *

c1 = card(1, "a")
c2 = card(2, "b")

print c1 == c2

set2 = deck(range(1,100))
set2.shuffle()
'''