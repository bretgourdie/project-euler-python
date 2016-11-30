import math

def maxSolutions(limit):
	maxSolution = (-1, -1)
	
	for p in range(1, limit+1):
		numSolutions = 0
		
		for a in range(1, p):
			for b in range(a, p):
				hyp2 = a ** 2 + b ** 2
				hyp = math.sqrt(hyp2)

				if a + b + hyp == p:
					numSolutions += 1
				
		if numSolutions > maxSolution[0]:
			maxSolution = (numSolutions, p)
	
	return maxSolution[1]


tests = [120, 1000]
for num in tests:
	print("The max solutions for p <= {} is p = {}".format(num, maxSolutions(num)))
