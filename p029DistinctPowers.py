def numDistinctPowers(limit):
	numList = {}
	for a in range(2, limit+1):
		for b in range(2, limit+1):
			term = a ** b

			if term not in numList:
				numList[term] = True
	
	return len(numList)

tests = [5, 100]
for num in tests:
	print("The number of distinct terms for a^b where 2 <= a <= {} and 2 <= b <= {} is {}".format(num, num, numDistinctPowers(num)))
