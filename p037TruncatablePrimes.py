from prime import getdPrimes

def findTruncatablePrimes(numPrimes):
	lPrimes = []
	dPrimes = getdPrimes(1000000)
	num = 11
	
	while len(lPrimes) < numPrimes:
		if max(dPrimes) < num:
			dPrimes = getdPrimes(num * 2)
		if num in dPrimes:
			sNum = str(num)
			lTrunc = sNum
			rTrunc = sNum
			isTruncatable = True
			for digit in sNum:
				lTrunc = lTrunc[1:]
				rTrunc = rTrunc[:-1]

				if len(lTrunc) > 0 and len(rTrunc) > 0:
					isTruncatable = isTruncatable and int(lTrunc) in dPrimes and int(rTrunc) in dPrimes

			if isTruncatable:
				lPrimes.append(num)
		num += 2
	
	return sum(lPrimes)

numTargetPrimes = 11
print("The sum of the {} primes that are truncatable is {}".format(numTargetPrimes, findTruncatablePrimes(numTargetPrimes)))
