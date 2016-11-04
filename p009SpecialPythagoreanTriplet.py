def getPythTriplet(total):
	for a in range(1, total):
		for b in range(a, total):
			for c in range(b, total):
				if a ** 2 + b ** 2 == c ** 2 and a + b + c == num:
					return a * b * c
	
	return -1

tests = [12]

for num in tests:
	print("The product for a+b+c=" + str(num) + " is " + str(getPythTriplet(num)))
