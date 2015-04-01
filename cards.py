#!/usr/bin/python
'''
Deck of arbitrary cards
'''
from numpy import random

#Hoyle cards
class card(object):   
	def __init__(self, number, suite):
		self.number = number
		self.suite = suite
	
	def suite(self):
		return self.suite
		
	def number(self):
		return self.number
	
	'''
	Almost always use str when creating output for end users.
	repr is mainly useful for debugging and exploring. 
	For example, if you suspect a string has non printing characters in it, 
	or a float has a small rounding error, repr will show you; str may not.
	'''
	def __repr__(self):
		return str(self.number) + " of " + self.suite

	def __str__(self):
		return str(self.number) + " of " + self.suite

class deck(card):
	cards = []
	def __init__(self, cards):
		self.size = len(cards)
		self.cards = cards
		
	#shuffle deck with random sort
	def shuffle(self):
		temp = [0]*self.size
		while 0 in temp:
			for x in self.cards:
				spot = int(random.rand()*self.size)
				if temp[spot] is 0 and x not in temp:
					temp[spot] = x
					(self.cards).remove(x)
		self.cards = temp
		
	def num(self):
		return self.size
		
	#get top of deck
	def top(self, num):
		#array accessor from beginning
		return self.cards[0:num]
		
	#get bottom of deck
	def bottom(self, num):
		#array accessor from end
		return self.cards[self.size:num+1:-1]
		
	#combine two decks
	def __add__ (self, cards):
		self.cards = self.cards + cards
		self.size += len(cards)