def findPrimeFactors(n):
	primeFactors = []
	ii = 2

	while ii <= n:
		while n % ii == 0:
			primeFactors.append(ii)
			n = n / ii
		ii += 1
	
	return primeFactors
