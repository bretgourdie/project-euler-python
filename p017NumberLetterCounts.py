import math

def getNumberLetterCount(toNum):
	sumLetters = 0

	for ii in range(1, toNum+1):
		print("Processing " + str(ii))
		strNum = str(ii)

		curStrNum = ""
		teen = False
		while len(strNum) > 0:
			curNum = strNum[0]

			if len(strNum) == 4:
				curStrNum += getThousandsDigit(curNum)
			elif len(strNum) == 3:
				curStrNum += getHundredsDigit(curNum, ii % 100 != 0)
			elif len(strNum) == 2:
				curStrNum += getTensDigit(curNum, strNum[1])
				teen = curNum == "1"
			elif len(strNum) == 1:
				if not teen:
					curStrNum += getOnesDigit(curNum)

			strNum = strNum[1:]

		print("Written out as \"{}\"; {} + {} = {}".format(curStrNum, sumLetters, len(curStrNum), sumLetters + len(curStrNum)))
		sumLetters += len(curStrNum)
	
	return sumLetters

def getOnesDigit(num):
	ones = {
		"0": "",
		"1": "one",
		"2": "two",
		"3": "three",
		"4": "four",
		"5": "five",
		"6": "six",
		"7": "seven",
		"8": "eight",
		"9": "nine"
		}
	
	return ones[num]

def getTensDigit(num, nextDigit):
	teens = {
		"0": "ten",
		"1": "eleven",
		"2": "twelve",
		"3": "thirteen",
		"4": "fourteen",
		"5": "fifteen",
		"6": "sixteen",
		"7": "seventeen",
		"8": "eighteen",
		"9": "nineteen"
		}
	tens = {
		"0": "",
		"1": teens,
		"2": "twenty",
		"3": "thirty",
		"4": "fourty",
		"5": "fifty",
		"6": "sixty",
		"7": "seventy",
		"8": "eighty",
		"9": "ninety"
		}
	
	ten = tens[num]
	if isinstance(ten, str):
		return ten
	else:
		return ten[nextDigit]

def getHundredsDigit(num, useAnd):
	if num == "0":
		return ""
	
	one = getOnesDigit(num)

	if useAnd:
		strAnd = "and"
	else:
		strAnd = ""
	
	return one + "hundred" + strAnd

def getThousandsDigit(num):
	if num == "0":
		return ""
	
	return getOnesDigit(num) + "thousand"

tests = [5, 1000]
for num in tests:
	print("The number of letters from 1 to {} is {}".format(num, getNumberLetterCount(num)))
