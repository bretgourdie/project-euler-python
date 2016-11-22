def findWays():
	rfindWays(0, 0, 0, 0, 0, 0, 0, 0, 200)

	numWays = 0

	for key in ways:
		if ways[key] == 0:
			numWays += 1

	return numWays

def rfindWays(p1, p2, p5, p10, p20, p50, lb1, lb2, remain):
	if (p1, p2, p5, p10, p20, p50, lb1, lb2) not in ways:
		ways[(p1, p2, p5, p10, p20, p50, lb1, lb2)] = remain
	
		if remain - 200 >= 0:
			rfindWays(p1, p2, p5, p10, p20, p50, lb1, lb2+1, remain-200)
		
		if remain - 100 >= 0:
			rfindWays(p1, p2, p5, p10, p20, p50, lb1+1, lb2, remain-100)
		
		if remain - 50 >= 0:
			rfindWays(p1, p2, p5, p10, p20, p50+1, lb1, lb2, remain-50)
		
		if remain - 20 >= 0:
			rfindWays(p1, p2, p5, p10, p20+1, p50, lb1, lb2, remain-20)
		
		if remain - 10 >= 0:
			rfindWays(p1, p2, p5, p10+1, p20, p50, lb1, lb2, remain-10)
		
		if remain - 5 >= 0:
			rfindWays(p1, p2, p5+1, p10, p20, p50, lb1, lb2, remain-5)
		
		if remain - 2 >= 0:
			rfindWays(p1, p2+1, p5, p10, p20, p50, lb1, lb2, remain-2)
		
		if remain - 1 >= 0:
			rfindWays(p1+1, p2, p5, p10, p20, p50, lb1, lb2, remain-1)

ways = {}
print("There are {} ways to make 2 pounds in change".format(findWays()))
