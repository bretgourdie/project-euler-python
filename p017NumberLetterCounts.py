def getNumberLetterCount(toNum):
	sumLetters = 0

	for ii in range(1, toNum+1):
		sumLetters += 1
	
	return sumLetters

tests = [5]
for num in tests:
	print("The number of letters from 1 to {} is {}".format(num, getNumberLetterCount(num)))
