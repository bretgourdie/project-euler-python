from itertools import permutations

def getLexographicPermutations(digits):
	perms = permutations(digits)

	return sorted(perms)

tests = [("012", 4), ("0123456789", 1000000)]
for digits in tests:
	print("The {}th permutation of {} is {}".format(\
	digits[1], digits[0], getLexographicPermutations(digits[0])[digits[1]-1]))
