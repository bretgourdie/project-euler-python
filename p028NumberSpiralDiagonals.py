def sumDiagonals(dimension):
	grid = generateGrid(dimension)

def generateGrid(dimension):
	grid = [[0 for x in range(dimension)] for y in range(dimension)]
	
	middle = dimension // 2
	cur = 1
	distance = 0
	direction = (1, 0) # right
	idx = middle
	jdx = middle

	directions = {
		( 1,  0) : ( 0,  1), # down
		( 0,  1) : (-1,  0), # left
		(-1,  0) : ( 0, -1), # up
		( 0, -1) : ( 1,  0)  # right
	}

	while cur <= dimension ** 2:
		if direction in [(-1,0),(1,0)]: # if left or right
			distance += 1
		for ii in range(min(distance, dimension)):
			grid[idx][jdx] = cur
			cur += 1
			idx += direction[1]
			jdx += direction[0]
		direction = directions[direction]
	
	return grid
		
tests = [5]
for num in tests:
	print("The sum of the numbers on the diagonals of a {}x{} spiral is {}".format(num, num, sumDiagonals(num)))
