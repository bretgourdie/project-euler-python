from prime import getPrimes
from pandigital import checkPandigital
import itertools

def getSumOfSubStringPandigitalNumbers(zeroToNPandigital, substringSize):
    numDigits = zeroToNPandigital + 1

    lPrimes = getPrimes(17)
    lPandigitalNumbers = []
    lSubStringPandigitalNumbers = []

    lPandigitalNumbers = itertools.permutations([str(num) for num in range(0, 9+1)])

    for tNum in lPandigitalNumbers:
        strNum = "".join(tNum)
        print(strNum)

    print("done")



    sumPandigital = sum(lSubStringPandigitalNumbers)

    return sumPandigital



tests = [(9,3)]
for tArgs in tests:
    print("The sum of all 0 to {} pandigital numbers with {} sub-string divisibility is {}".format(tArgs[0], tArgs[1], getSumOfSubStringPandigitalNumbers(tArgs[0], tArgs[1])))
