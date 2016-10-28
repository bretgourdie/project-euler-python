def findPalindrome (digits):
	limit = 10 ** digits - 1
	first = limit
	second = limit

	maxPalindrome = -1

	while first >= 1:
		while second >= 1:
			
			product = first * second

			if(isPalindrome(product)):
				maxPalindrome = max(maxPalindrome, product)
			
			second -= 1

		first -= 1
	
	return maxPalindrome

def isPalindrome (number):
	strNumber = str(number)

	return list(strNumber) == list(reversed(strNumber))

testCases = [2]

for num in testCases:
	print("The max palindrome for " + str(num) + " is " + str(findPalindrome(num)))
