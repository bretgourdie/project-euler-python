from math import factorial

def factorialSumDigits(num):
	fact = factorial(num)
	
	sum = 0
	for letter in str(fact):
		sum += int(letter)

	return sum

tests = [10, 100]

for num in tests:
	print("The sum of the factorial digits in {} is {}".format(num, factorialSumDigits(num)))
