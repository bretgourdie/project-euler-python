from decimal import *

def findLongestCycle(toNum):
	maxD = -1
	maxDLen = -1

	for num in range(2, toNum):
		foundCycle = False
		terminated = False
		remainderList = []
		remainder = 1
		while not foundCycle and not terminated:
			while remainder < num:
				remainder *= 10
			
			remainder %= num
			terminated = remainder == 0
			foundCycle = remainder in remainderList
			remainderList.append(remainder)
		
		if foundCycle:
			firstIndex = remainderList.index(remainderList[-1])
			length = len(remainderList) - firstIndex - 1
			if length > maxDLen:
				maxD = num
				maxDLen = length

	return maxD

tests = [11]
for num in tests:
	print("The value of d with the longest recurring cycle where d < {} is {}".format(num, findLongestCycle(num)))
