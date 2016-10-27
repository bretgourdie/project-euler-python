from prime import *

testCases = [13195, 600851475143]

for num in testCases:
	print("Largest prime factor of "
	 + str(num) + " is " + str(max(findPrimeFactors(num))))
