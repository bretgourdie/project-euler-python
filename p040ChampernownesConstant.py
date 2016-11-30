from decimal import *

getcontext().prec = 1000000+2
champ = Decimal(60499999499) / Decimal(490050000000)

sChamp = str(champ)

d = 1
dx = 1

while dx <= 1000000:
	d *= int(sChamp[dx + 1])
	dx *= 10

print("d = {}".format(d))
