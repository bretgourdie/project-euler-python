def findFiboIndex(numDigits):
	prev = 0
	cur = 1
	index = 1

	while len(str(cur)) < numDigits:
		new = cur + prev
		prev = cur
		cur = new
		index += 1
	
	return index

tests = [3]
for num in tests:
	print("The first index to contain {} digits is {}".format(num, findFiboIndex(num)))
