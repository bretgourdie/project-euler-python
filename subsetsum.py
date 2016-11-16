def findSubsetSum(subset, targetSum, index = 0, memo = {}):
	if index >= len(subset): return 1 if targetSum == 0 else 0

	if (index, targetSum) not in memo:
		count = findSubsetSum(subset, targetSum, index + 1, memo)
		count += findSubsetSum(subset, targetSum - subset[index], index + 1, memo)
		memo[(index, targetSum)] = count
	return memo[(index, targetSum)]


