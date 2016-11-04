def longestCollatz(below):
	longestSeq = -1
	longestTerm = 1

	for ii in range(1, below, 2):
		curSeq = 1
		curTerm = ii

		while curTerm > 1:
			if curTerm % 2 == 0:
				curTerm //= 2
			else:
				curTerm = 3 * curTerm + 1
			curSeq += 1
		
		if curSeq > longestSeq:
			longestTerm = ii
		longestSeq = max(curSeq, longestSeq)
	
	return longestTerm

tests = [14, 1000000]

for num in tests:
	print("The longest chain for numbers under " + str(num) + " is " + str(longestCollatz(num)))
