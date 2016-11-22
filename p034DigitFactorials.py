from math import factorial

def findDigitFactorials():
	iSum = 0
	for num in range(10, 9999999):
		sNum = str(num)
		curSum = 0
		for digit in sNum:
			curSum += factorial(int(digit))

		if curSum == num:
			iSum += num

	return iSum

print("The sum of all numbers which are equal to the sum of the factorial of their digits is {}".format(findDigitFactorials())
