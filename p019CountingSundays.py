from datetime import date

def getNumSundays(year):
	numSundays = 0
	curDate = date(year, 1, 1)
	while curDate.year < 2001:
		if curDate.weekday() == 6:
			numSundays += 1

		if curDate.month == 12:
			curDate = date(curDate.year + 1, 1, 1)
		else:
			curDate = date(curDate.year, curDate.month + 1, 1)
	return numSundays


tests = [1991, 1901]

for num in tests:
	print("The number of Sundays in {} falling on the first of the month is {}".format(num, getNumSundays(num)))
