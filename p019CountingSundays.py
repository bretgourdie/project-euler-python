def getNumSundays(year):
	return -1

tests = [2007]

for num in tests:
	print("The number of Sundays in {} falling on the first of the month is {}".format(num, getNumSundays(num)))
