def findPaths(length, width):
	
	if length < 0 or width < 0:
		return 0
	
	if length == 0 and width == 0:
		return 1
	
	return findPaths(length - 1, width) + findPaths(length, width - 1)
	
tests = [2, 20]

for num in tests:
	print("A " + str(num) + "x" + str(num) + " grid has " + str(findPaths(num, num)) + " paths.")
