from itertools import permutations

def getLexographicPermutations(digits):
	perms = permutations(digits)

	return sorted(perms)

tests = ["012"]
for digits in tests:
	print("The permutations of {} are {}".format(digits, getLexographicPermutations(digits)))
