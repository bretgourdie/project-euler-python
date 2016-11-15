def getNumSundays(year):
	daysInMonth = {
		 0 : 31,
		 1 : 28,
		 2 : 31,
		 3 : 30,
		 4 : 31,
		 5 : 30,
		 6 : 31,
		 7 : 31,
		 8 : 30,
		 9 : 31,
		10 : 30,
		11 : 31 
	}

	dayOfWeek = 1 # Jan 1 of "year" must be a Tuesday
	monthOfYear = 0 # Start in January
	numSundays = 0
	leapYearDay = 0

	while year < 2001:
		if dayOfWeek == 6:
			numSundays += 1
		
		dayOfWeek = (dayOfWeek + daysInMonth[monthOfYear] + leapYearDay) % 7
		monthOfYear = (monthOfYear + 1) % 12

		if monthOfYear == 0:
			year += 1
		if monthOfYear == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
			leapYearDay = 1
		else:
			leapYearDay = 0

	return numSundays


tests = [1991, 1901]

for num in tests:
	print("The number of Sundays in {} falling on the first of the month is {}".format(num, getNumSundays(num)))
