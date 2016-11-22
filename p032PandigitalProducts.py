from collections import defaultdict

def checkPandigital(multiplicand, multiplier, product):
	sRes = str(product) + str(multiplicand) + str(multiplier)
	nums = "0123456789"

	for num in nums:
		if int(num) > 0:
			if sRes.count(num) != 1:
				return False
		elif int(num) == 0:
			if sRes.count(num) > 0:
				return False
	
	return True

def getPandigitalSum():
	dResults = {}

	for multiplicand in range(2, 9999):
		for multiplier in range(2, 9999):
			product = multiplicand * multiplier
			if checkPandigital(multiplicand, multiplier, product):
				dResults[product] = (multiplicand, multiplier)
	
	keys = dResults.keys()

	return sum(keys)

print("The sum of all products whose multiplicant/multipler/product identity can be written as a 1 through 9 pandigital is {}".format(getPandigitalSum()))
