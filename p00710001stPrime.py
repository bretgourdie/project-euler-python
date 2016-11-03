import prime

def getPrime(xth):
	primes = prime.getPrimes(xth ** 2)

	return primes[xth-1]

tests = [6, 10001]

for num in tests:
	print("Prime number " + str(num) + " is " + str(getPrime(num)))
