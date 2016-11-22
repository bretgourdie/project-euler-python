from collections import defaultdict

def checkPandigital(multiplicand, multiplier, product):
	sRes = str(product) + str(multiplicand) + str(multiplier)
	nums = "123456789"

	for num in nums:
		if sRes.count(num) != 1:
			return False
	
	return True

def getPandigitalSum():
	dResults = {}

	for multiplicand in range(1, 987654321):
		for multiplier in range(1, 493827161):
			product = multiplicand * multiplier
			if checkPandigital(multiplicand, multiplier, product):
				dResults[product] = (multiplicand, multiplier)
	
	
	keys = dResults.keys()

	return sum(keys)

print("The sum of all products whose multiplicant/multipler/product identity can be written as a 1 through 9 pandigital is {}".format(getPandigitalSum()))
