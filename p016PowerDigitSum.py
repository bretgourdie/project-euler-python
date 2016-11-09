def powerDigitSum(exponent):
	power = 2 ** exponent

	strPower = str(power)

	sum = 0
	for letter in strPower:
		sum += int(letter)
	
	return sum
	
tests = [15, 1000]
for num in tests:
	print("The sum of the digits of 2^{} = {}".format(num, powerDigitSum(num)))
