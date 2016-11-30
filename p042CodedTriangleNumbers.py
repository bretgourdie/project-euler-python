import csv

def isTriangleNumber(wordValue):
	triangleNumber = -1
	n = 0
	while triangleNumber < wordValue:
		triangleNumber = n / 2 * (1 + n)
		n += 1

	return triangleNumber == wordValue

triangleWords = []
wordFile = "p042_words.txt"
with open(wordFile, "r") as fWordFile:
	reader = csv.reader(fWordFile)
	lWordFile = list(reader)

lWordList = lWordFile[0]

for word in lWordList:
	wordValue = 0
	for letter in word:
		wordValue += ord(letter) - ord('A') + 1
	
	if isTriangleNumber(wordValue):
		triangleWords.append(word)

print("The number of word values that are triangle numbers is {}".format(len(triangleWords)))
	

