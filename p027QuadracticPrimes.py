from prime import getPrimes

def findQuadExp(limit):
	maxNumPrimes = -1
	product = -1
	
	primes = getPrimes(limit ** 2 + 999 * limit + 1000)
	
	for a in range(limit):
		for b in range(limit + 1):
			primeCount = 0
			for n in range(limit+1):
				num = n ** 2 + a * n + b
				if num in primes:
					primeCount += 1
					
			
			if primeCount > maxNumPrimes:
				maxNumPrimes = primeCount
				product = a * b
			
	return product

tests = [41]
for num in tests:
	print("The product producing the maximum number of primes where n <= {} is {}".format(num, findQuadExp(num)))
