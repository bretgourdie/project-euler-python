import math

def getNumberLetterCount(toNum):
	sumLetters = 0

	for ii in range(1, toNum+1):
		print("Processing " + str(ii))
		strNum = str(ii)

		while len(strNum) > 0:
			numLetters = 0
			curNum = strNum[0]
			print("curNum = " + curNum)

			if len(strNum) == 4:
				numLetters += getThousandsDigit(curNum, ii % 1000 != 0)
				print("Got thousands digit as " + str(numLetters))
			if len(strNum) == 3:
				numLetters += getHundredsDigit(curNum, ii % 100 != 0)
				print("Got hundreds digit as " + str(numLetters))
			if len(strNum) == 2:
				numLetters += getTensDigit(curNum)
				print("Got tens digit as " + str(numLetters))
			if len(strNum) == 1:
				numLetters += getOnesDigit(curNum)
				print("Got ones digit as " + str(numLetters))

			strNum = strNum[1:]

		sumLetters += numLetters
	
	return sumLetters

def getOnesDigit(num):
	num = int(num)
	wordLetters = 0
	if num == 1 or num == 2 or num == 6:
		wordLetters = 3
	elif num == 4 or num == 5 or num == 9:
		wordLetters = 4
	elif num == 3 or num == 7 or num == 8:
		wordLetters = 5
	
	return wordLetters

def getTensDigit(num):
	num = int(num)
	wordLetters = 0
	if num == 1:
		return 6
	if (num >= 2 and num <= 4) or num == 8 or num == 9:
		wordLetters = 6
	elif num == 5 or num == 6:
		wordLetters = 5
	elif num == 7:
		wordLetters = 7
	
	return wordletters

def getHundredsDigit(num, useAnd):
	num = int(num)
	single = getOnesDigit(num)

	hundred = len("hundred")

	if useAnd:
		iAnd = len("and")
	else:
		iAnd = 0

	return single + hundred + iAnd

def getThousandsDigit(num, useAnd):
	num = int(num)
	single = getOnesDigit(num)

	thousand = len("thousand")

	if useAnd:
		iAnd = len("and")
	else:
		iAnd = 0
	
	return single + thousand + iAnd

tests = [5]
for num in tests:
	print("The number of letters from 1 to {} is {}".format(num, getNumberLetterCount(num)))
