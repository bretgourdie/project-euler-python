def cancellable(num, dem):
	dec = num / dem
	
	for d1 in str(num):
		for d2 in str(dem):
			if d1 == d2:
				sNewNum = str(num).replace(d1, "", 1)
				sNewDem = str(dem).replace(d2, "", 1)
				newNum = int(sNewNum)
				newDem = int(sNewDem)

				if newDem > 0 and newNum != newDem and newNum / newDem == dec:
					return True
	
	return False

def findCancellingFractions(numToFind):
	fractions = []
	
	for num in range(10, 99):
		for dem in range(10, 99):
			if num < dem and (num % 10 != 0 or dem % 10 != 0) and cancellable(num, dem):
				fractions.append((num,dem))
	
	if len(fractions) != numToFind:
		print("len(fractions) == {} != {}".format(len(fractions), numToFind))
	
	num = 1
	dem = 1
	for fracs in fractions:
		num *= fracs[0]
		dem *= fracs[1]
	
	return (num, dem)

tests = [4]
for num in tests:
	print("The denominator of the {} cancelling fractions is {}".format(num, findCancellingFractions(num)))
