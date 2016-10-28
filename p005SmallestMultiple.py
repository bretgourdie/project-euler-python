def smallestMultiple(limit):
	
	multiple = 1
	found = False

	while not found:
		goodSoFar = True
	
		for num in range(1, limit + 1):
			if multiple % num != 0:
				goodSoFar = False
				break

		if goodSoFar:
			found = True
		else:
			multiple += 1
	
	return multiple

testCases = [10, 20]

for num in testCases:
	print("The smallest positive number that is evenly divisible by numbers from 1 to " + str(num) 
	+ " is " 
	+ str(smallestMultiple(num)))
