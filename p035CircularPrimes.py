from math import ceil, log
from prime import getPrimes

def getCircularPrimes(limit):
	primes = getPrimes(limit)
	dPrimes = dict(zip(primes, [True] * len(primes)))

	circularPrimes = []
	for num in range(2, limit):
		if num in dPrimes:
			numDigits = ceil(log(num))
			sCurNum = str(num)
			isCircular = True
			for ii in range(numDigits):
				sCurNum = sCurNum[1:] + sCurNum[0]
				iCurNum = int(sCurNum)
				isCircular = isCircular and iCurNum in dPrimes

			if isCircular:
				circularPrimes.append(num)

	return len(circularPrimes)

tests = [100]
for num in tests:
	print("There are {} circular primes below {}".format(getCircularPrimes(num), num))
