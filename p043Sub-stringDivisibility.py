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
            primeSubStringDivisibility = True
            for startDigit in range(1, numDigits - substringSize + 1):
                strNum = str(num)
                lDigits = []
                for offset in range(0, substringSize):
                    lDigits.append(strNum[startDigit + offset])

                strSubstring = ''.join(lDigits)
                iSubstring = int(strSubstring)

                numPrimeToDivideBy = startDigit - 1
                primeToDivideBy = lPrimes[numPrimeToDivideBy]
                isDivisible = iSubstring % primeToDivideBy == 0
                
                primeSubStringDivisibility = primeSubStringDivisibility and isDivisible

                #print("Digits {} become {} which is divisible by the {}th prime {}? {}".format(lDigits, iSubstring, numPrimeToDivideBy+1, primeToDivideBy, isDivisible))

                if not primeSubStringDivisibility:
                    break

            if primeSubStringDivisibility:
                print("\"{}\" was fully divisible".format(num))
                lSubStringPandigitalNumbers.append(num)

    
    sumPandigital = sum(lSubStringPandigitalNumbers)

    return sumPandigital



tests = [(9,3)]
for tArgs in tests:
    print("The sum of all 0 to {} pandigital numbers with {} sub-string divisibility is {}".format(tArgs[0], tArgs[1], getSumOfSubStringPandigitalNumbers(tArgs[0], tArgs[1])))
