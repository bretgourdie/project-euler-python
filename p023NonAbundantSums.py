from divisors import findProperDivisors

def findNonAbundantSums(num):
	abundantSums = 0
	
	abundantNums = []
	for ii in range(1, (num+1) // 2):
		divisors = findProperDivisors(ii)
		if sum(divisors) > ii:
			abundantNums.append(ii)
	
	return abundantSums

tests = [28123]
for num in tests:
	print("The sum of all positive integers that cannot be written as the sum of two abundant numbers is {}".format(findNonAbundantSums(num)))
