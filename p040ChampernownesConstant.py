def createChamp(limit):
	champ = "."

	for num in range(1, limit+1):
		champ += str(num)
	
	return champ

d = 1
dx = 1
sChamp = createChamp(1000000)

while dx <= 1000000:
	d *= int(sChamp[dx + 1])
	dx *= 10

print("d = {}".format(d))
