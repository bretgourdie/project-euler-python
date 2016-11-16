from divisors import findProperDivisors

def findNonAbundantSums(num):
	abundantSum = 0
	
	abundantNums = []
	for abundantNumCandidate in range(1, num+1):
		divisors = findProperDivisors(abundantNumCandidate)
		if sum(divisors) > abundantNumCandidate:
			abundantNums.append(abundantNumCandidate)
	
	abundantSums = {}
	for fNum in abundantNums:
		for sNum in abundantNums:
			abundantSums[fNum + sNum] = True
	
	for ii in range(1, num+1):
		if ii not in abundantSums:
			abundantSum += ii

	return abundantSum

tests = [28123]
for num in tests:
	print("The sum of all positive integers that cannot be written as the sum of two abundant numbers is {}".format(findNonAbundantSums(num)))
