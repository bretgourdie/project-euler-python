import math

def isPrime(n):
	if n < 2:
		return False
	if n % 2 == 0:
		return n == 2
	
	root = math.sqrt(n)

	for ii in range(3, int(root)+1, 2):
		if n % ii == 0:
			return False
	
	return True
	
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

	for idx, numIsPrime in enumerate(primeSieve):
		if numIsPrime:
			curNumber = idx+1
			curNumberSquared = curNumber ** 2
			curNumberIndex = curNumberSquared - 1

			while curNumberIndex < len(primeSieve):
				primeSieve[curNumberIndex] = False
				curNumberIndex += curNumber
	
	return primeSieve



def convertSieveToPrimes(sieve):
	primes = []

	for index, numIsPrime in enumerate(sieve):
		if numIsPrime:
			primes.append(index+1)
	
	return primes
