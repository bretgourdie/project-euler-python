def getTriangleNumber(numDivisors):
	return -1

tests = [5]

for num in tests:
	print("The value of the first triange number to have over " + str(num) + " divisors is "\
	+ str(getTriangleNumber(num)))
