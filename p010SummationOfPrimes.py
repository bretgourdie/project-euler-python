import prime

def primesSum(below):
	primes = prime.getPrimes(below)

	total = sum(primes)

	return total

tests = [10, 2000000]

for num in tests:
	print("The sum of primes below " + str(num) + " is " + str(primesSum(num)))
