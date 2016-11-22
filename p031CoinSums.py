def findWays():
	rfindWays((0, 0, 0, 0, 0, 0, 0, 0), 200)
	
	numWays = 0
	
	for key in ways:
		if ways[key] == 0:
			numWays += 1
	
	return numWays

def rfindWays(curCoinList, remain):
	if curCoinList not in ways:
		ways[curCoinList] = remain
		
		for idx,coin in enumerate(coins):
			if remain - coin >= 0:
				newCoin = (curCoinList[idx] + 1,)
				newCoinList = curCoinList[:idx] + newCoin + curCoinList[idx+1:]
				rfindWays(newCoinList, remain-coin)

ways = {}
coins = (1, 2, 5, 10, 20, 50, 100, 200)
print("There are {} ways to make 2 pounds in change".format(findWays()))
