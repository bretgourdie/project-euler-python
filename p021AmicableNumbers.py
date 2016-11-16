from divisors import findProperDivisors

def sumAmicableNumbers(limit):
	sumAmicable = 0
	for ii in range(1, limit):
		curProperDivisors = findProperDivisors(ii)
		curSum = sum(curProperDivisors)
		
		if curSum != ii:
			sumProperDivisors = findProperDivisors(curSum)

			if sum(sumProperDivisors) == ii:
				sumAmicable += ii
	
	return sumAmicable

tests = [285, 10000]
for num in tests:
	print("The sum of all amicable numbers below {} is {}".format(num, sumAmicableNumbers(num)))
