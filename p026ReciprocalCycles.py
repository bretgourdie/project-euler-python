from decimal import *

class Trie:
	def __init__(self, value=None, substrings=None):
		self.value = value
		self.substrings = substrings
	
	def __str__(self):
		if substrings == None:
			return self.value
		else:
			return substrings

def findLongestCycle(toNum):
	for num in range(2, toNum):
		fraction = Decimal(1) / Decimal(num)

		sFraction = str(fraction)

		if sFraction[:2] == "0.":
			sFraction = sFraction[2:]

		print("Fraction part = {}".format(sFraction))
		
		trie = createTrie(sFraction)
	
	return -1

def createTrie(fraction):
	tFraction = fraction + "$"
	root = Trie(value="")



tests = [11]
for num in tests:
	print("The value of d with the longest recurring cycle where d < {} is {}".format(num, findLongestCycle(num)))
