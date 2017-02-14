from pandigital import checkPandigital

def getSumOfSubStringPandigitalNumbers(zeroToNPandigital):
    numDigits = zeroToNPandigital + 1

    startingNumber = 10 ** zeroToNPandigital
    endingNumber = 10 ** numDigits
    for num in range(startingNumber, endingNumber):
        isPandigital = checkPandigital(num, zeroToNPandigital)


tests = [(9,3)]
for tArgs in tests:
    print("The sum of all 0 to {} pandigital numbers with {} sub-string divisibility is {}".format(tArgs[0], tArgs[1], getSumOfSubStringPandigitalNumbers(tArgs[0], tArgs[1])))
