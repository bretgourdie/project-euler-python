
def checkPandigital(product):
	nums = "0123456789"

	for num in nums:
		if int(num) > 0:
			if product.count(num) != 1:
				return False
		elif int(num) == 0:
			if product.count(num) > 0:
				return False
	return True

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

			if checkPandigital(sNum):
				largestPan = max(largestPan, int(sNum))

			n += 1

	return largestPan


tests = [9, 100000]
for num in tests:
	print("The largest 1 to {} pandigital {}-digit number is {}".format(num, num, findLargestPandigital(num)))
