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

        endDigit = len(strNum) - substringSize

        hasBeenSubstringPandigital = True
        for curDigit in range(1, endDigit+1):
            curPrime = lPrimes[curDigit-1]
            curEndDigit = curDigit + substringSize
            curNumber = int(strNum[curDigit:curEndDigit])

            isSubstringPandigital = curNumber % curPrime == 0

            hasBeenSubstringPandigital = isSubstringPandigital and hasBeenSubstringPandigital

        if hasBeenSubstringPandigital:
            lSubStringPandigitalNumbers.append(int(strNum))


    sumPandigital = sum(lSubStringPandigitalNumbers)

    return sumPandigital



tests = [(9,3)]
for tArgs in tests:
    print("The sum of all 0 to {} pandigital numbers with {} sub-string divisibility is {}".format(tArgs[0], tArgs[1], getSumOfSubStringPandigitalNumbers(tArgs[0], tArgs[1])))
