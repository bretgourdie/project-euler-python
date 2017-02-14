from prime import getPrimes
from pandigital import checkPandigital

def getSumOfSubStringPandigitalNumbers(zeroToNPandigital, substringSize):
    numDigits = zeroToNPandigital + 1

    #startingNumber = 10 ** zeroToNPandigital
    startingNumber = 1023456789
    endingNumber = 10 ** numDigits
    lPrimes = getPrimes(17)
    lSubStringPandigitalNumbers = []

    for num in range(startingNumber, endingNumber):
        isPandigital = checkPandigital(num, zeroToNPandigital, includeZero=True)

        if isPandigital:
            print("\"{}\" is pandigital".format(num))
            primeSubStringDivisibility = True
            for startDigit in range(substringSize - 1, numDigits - substringSize):
                strNum = str(num)
                lDigits = []
                for offset in range(0, substringSize):
                    lDigits.append(strNum[startDigit + offset])

                strSubstring = ''.join(lDigits)
                iSubstring = int(strSubstring)

                primeToDivideBy = lPrimes[startDigit - substringSize + 1]
                isDivisible = iSubstring % primeToDivideBy == 0
                
                primeSubStringDivisibility = primeSubStringDivisibility and isDivisible

                print("Digits {} become {} which is divisible by {}? {}".format(lDigits, iSubstring, primeToDivideBy, isDivisible))

            print("\"{}\" was fully divisible? {}".format(num, primeSubStringDivisibility))
            if primeSubStringDivisibility:
                lSubStringPandigitalNumbers.append(num)

    
    sumPandigital = sum(lSubStringPandigitalNumbers)

    return sumPandigital



tests = [(9,3)]
for tArgs in tests:
    print("The sum of all 0 to {} pandigital numbers with {} sub-string divisibility is {}".format(tArgs[0], tArgs[1], getSumOfSubStringPandigitalNumbers(tArgs[0], tArgs[1])))
