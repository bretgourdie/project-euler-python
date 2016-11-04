import math

def getTriangleNumber(numDivisors):
	foundTriangleNumber = False
	startingNumber = 0

	while not foundTriangleNumber:
		startingNumber += 1
		curTriangleNumber = 0
		for ii in range(1, startingNumber+1):
			curTriangleNumber += ii

		numFoundDivisors = 0
		limit = math.sqrt(curTriangleNumber)
		ii = 1
		while (ii <= limit):
			if curTriangleNumber % ii == 0:
				numFoundDivisors += 1

				if ii != curTriangleNumber // ii:
					numFoundDivisors += 1
			ii += 1

		foundTriangleNumber = numFoundDivisors >= numDivisors
	
	return curTriangleNumber

tests = [5]#, 500]

for num in tests:
	print("The value of the first triange number to have over " + str(num) + " divisors is "\
	+ str(getTriangleNumber(num)))
