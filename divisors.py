from math import sqrt

def findDivisors(num):
	divisors = []
	limit = sqrt(num)
	ii = 1

	while ii <= limit:
		if num % ii == 0:
			divisors.append(ii)
			
			if ii != num // ii:
				divisors.append(num // ii)

		ii += 1
	
	return sorted(divisors)

def findProperDivisors(num):
	divisors = findDivisors(num)
	
	if num in divisors:
		divisors.remove(num)
	else:
		print("{} not in {}!".format(num, divisors))

	return divisors
