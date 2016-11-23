from prime import isPrime

def findTruncatablePrimes(numPrimes):
	lPrimes = []
	num = 37
	dPrimes = getdPrimes(10 ** 8)
	while len(lPrimes) < numPrimes:
		if isPrime(num):
			sNum = str(num)
			slTrunc = sNum
			srTrunc = sNum
			isTruncatable = True
			for digit in sNum:
				slTrunc = slTrunc[1:]
				srTrunc = srTrunc[:-1]
				lTrunc = int(slTrunc)
				rTrunc = int(srTrunc)

				if len(slTrunc) > 0 and len(srTrunc) > 0:
					isTruncatable = isTruncatable and lTrunc in dPrimes and rTrunc in dPrimes
					if not isTruncatable:
						break

			if isTruncatable:
				lPrimes.append(num)
		num += 2
	
	return sum(lPrimes)

numTargetPrimes = 11
print("The sum of the {} primes that are truncatable is {}".format(numTargetPrimes, findTruncatablePrimes(numTargetPrimes)))
