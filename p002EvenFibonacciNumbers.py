from fibo import *

def sumEvenValues(limit):
	fiboRange = fibValueTo(limit)
	sum = 0

	for num in fiboRange:
		if num % 2 == 0:
			sum += num
	
	return sum

print("Sum of even Fibonacci numbers to 10: " + str(sumEvenValues(89)))
print("Sum of even Fibonacci numbers to 4000000: " + str(sumEvenValues(4000000)))
