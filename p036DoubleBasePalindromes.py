def doubleBasePalindromes(num):
	lPal = []

	for dNum in range(1, num):
		sbNum = "{0:b}".format(dNum)

		if str(dNum) == str(dNum)[::-1] and sbNum == sbNum[::-1]:
			lPal.append(dNum)

	return sum(lPal)

tests = [1000]
for num in tests:
	print("The sum of all numbers less than {} which are palindromic in base 10 and base 2 is {}".format(num, doubleBasePalindromes(num)))
