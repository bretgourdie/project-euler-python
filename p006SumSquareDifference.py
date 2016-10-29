def sumSquareDifference(limit):
	sumOfSquares = 0
	squareOfSums = 0
	for num in range(1, limit+1):
		sumOfSquares += num ** 2
		squareOfSums += num
	
	squareOfSums **= 2
	
	return squareOfSums - sumOfSquares

tests = [10, 100]

for num in tests:
	print("The difference between the sum of the squares of the first " 
	+ str(num)
	+ " natural numbers and the square of the sum is " + str(sumSquareDifference(num)))
