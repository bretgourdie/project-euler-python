import csv

def getNameScores(nameFile):
	score = 0
	with open(nameFile, "r") as fNameFile:
		reader = csv.reader(fNameFile)
		lNameFile = list(reader)
	
	lNameList = lNameFile[0]
	
	lNameList.sort()

	for ii,name in enumerate(lNameList):
		nameScore = 0
		for letter in name:
			nameScore += ord(letter) - ord('@')
		score += nameScore * (ii+1)
	return score

tests = ["p022_names.txt"]

for nameFile in tests:
	print("The total of all the name scores in {} is {}".format(nameFile, getNameScores(nameFile)))
