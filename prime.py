def findPrimeFactors(n):
	primeFactors = []
	ii = 2

	for ii in range(2, n):
		while n % ii == 0:
			primeFactors.append(ii)
			n = n / ii
	
	return primeFactors
