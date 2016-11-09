def findPaths(length, width):

	if length < 0 or width < 0:
		return 0
	
	if length == 0 and width == 0:
		return 1

	lengthKey = str(length - 1) + "," + str(width)
	widthKey = str(length) + "," + str(width - 1)
	
	if lengthKey in triedPaths:
		lengthPaths = triedPaths[lengthKey]
	else:
		lengthPaths = findPaths(length - 1, width)
		triedPaths[lengthKey] = lengthPaths
	if widthKey in triedPaths:
		widthPaths = triedPaths[widthKey]
	else:
		widthPaths = findPaths(length, width - 1)
		triedPaths[widthKey] = widthPaths
	
	return lengthPaths + widthPaths
	
tests = [2]
triedPaths = {}

for num in tests:
	print("A " + str(num) + "x" + str(num) + " grid has " + str(findPaths(num, num)) + " paths.")
