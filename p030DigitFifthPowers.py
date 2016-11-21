def digitPowers(numDigits):
	limit = 10 ** (numDigits+1)
	sumDigitPowers = 0

	for ii in range(2, limit):
		curSum = 0
		curNum = ii
		while curNum > 0:
			curDigit = curNum % 10
			curNum //= 10
			curSum += curDigit ** numDigits

		if curSum == ii:
			sumDigitPowers += ii
			print("{}; {}".format(ii, sumDigitPowers))
	
	return sumDigitPowers

tests = [4, 5]
for num in tests:
	print("The sum of the numbers that can be written as the sum of {}th powers of their digits is {}".format(num, digitPowers(num)))
