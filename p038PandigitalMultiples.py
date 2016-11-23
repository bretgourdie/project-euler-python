import pandigital

def findLargestPandigital(limit):
	largestPan = -1
	sNum = ""
	for num in range(1, limit+1):
		sNum = "1"
		n = 2
		while len(sNum) <= 9:
			sNum = ""
			for ii in range(1, n+1):
				sNum += str(num * ii)

			if pandigital.checkPandigital(sNum, 9):
				largestPan = max(largestPan, int(sNum))

			n += 1

	return largestPan


tests = [9, 100000]
for num in tests:
	print("The largest 1 to {} pandigital {}-digit number is {}".format(num, num, findLargestPandigital(num)))
