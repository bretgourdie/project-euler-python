from collections import defaultdict
import pandigital

def getPandigitalSum():
	dResults = {}

	for multiplicand in range(2, 9999):
		for multiplier in range(2, 9999):
			product = multiplicand * multiplier
			num = str(multiplicand) + str(multiplier) + str(product)
			if pandigital.checkPandigital(num, 9):
				dResults[product] = (multiplicand, multiplier)
	
	keys = dResults.keys()

	return sum(keys)

print("The sum of all products whose multiplicant/multipler/product identity can be written as a 1 through 9 pandigital is {}".format(getPandigitalSum()))
