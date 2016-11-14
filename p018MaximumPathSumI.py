class Tree:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
	
	def __str__(self):
		return str(self.value)

def findMaxPath(test):

	if test == 1:
		strTriangle = genFirstTest()
	elif test == 2:
		strTriangle = genSecondTest()
	
	triangle = genTree(strTriangle)


def genFirstTest():
	strTree = \
"""\
3
7 4
2 4 6
8 5 9 3\
"""
	return strTree

def genSecondTest():
	strTree = \
"""\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23\
"""

def genTree(strTriangle):
	splitTriangle = strTriangle.splitlines()
	splitTriangle.reverse()
	numElements = splitTriangle[0].count(' ') + 1
	nextLineQueue = []
	queue = []
	for line in splitTriangle:
		elements = line.split(' ')

		for elm in elements:
			curLeft = None
			curRight = None
			if len(queue) > 0:
				curLeft = queue.pop(0)
				curRight = queue[0]
			
			tree = Tree(int(elm), curLeft, curRight)
			nextLineQueue.append(tree)
			
		queue = list(nextLineQueue)
		nextLineQueue = []
	
	return tree

tests = [1]
for num in tests:
	print("The maximum total from top to bottom of test {} is {}".format(num, findMaxPath(num)))
