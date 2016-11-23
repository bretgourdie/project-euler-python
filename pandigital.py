
def checkPandigital(product, checkToNumber):
	numList = list(range(0, checkToNumber+1))
	nums = ''.join(str(num) for num in numList)
	sProduct = str(product)

	for num in nums:
		if int(num) > 0:
			if sProduct.count(num) != 1:
				return False
		elif int(num) == 0:
			if sProduct.count(num) > 0:
				return False
	return True

