from divisors import findProperDivisors
from subsetsum import findSubsetSum

def findNonAbundantSums(num):
	abundantSums = 0
	
	abundantNums = []
	for ii in range(1, (num+1) // 2):
		divisors = findProperDivisors(ii)
		if sum(divisors) > ii:
			abundantNums.append(ii)
	
	for ii in range(1, num+1):
		if findSubsetSum(abundantNums, ii) == 0:
			abundantSums += ii
	
	return abundantSums

tests = [28123]
for num in tests:
	print("The sum of all positive integers that cannot be written as the sum of two abundant numbers is {}".format(findNonAbundantSums(num)))
