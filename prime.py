def findPrimeFactors(n):
	primeFactors = []
	ii = 2

	while ii <= n:
		while n % ii == 0:
			primeFactors.append(ii)
			n = n / ii
		ii += 1
	
	return primeFactors

def getPrimes(n):
	primeSieve = createPrimeSieve(n)

	primes = convertSieveToPrimes(primeSieve)

	return primes

def getdPrimes(n):
	primes = getPrimes(n)

	dPrimes = dict(zip(primes, [True] * len(primes)))

	return dPrimes

def createPrimeSieve(n):
	primeSieve = [True] * n
	
	if len(primeSieve) > 0:
		primeSieve[0] = False

	for idx, isPrime in enumerate(primeSieve):
		if isPrime:
			curNumber = idx+1
			curNumberSquared = curNumber ** 2
			curNumberIndex = curNumberSquared - 1

			while curNumberIndex < len(primeSieve):
				primeSieve[curNumberIndex] = False
				curNumberIndex += curNumber
	
	return primeSieve



def convertSieveToPrimes(sieve):
	primes = []

	for index, isPrime in enumerate(sieve):
		if isPrime:
			primes.append(index+1)
	
	return primes
