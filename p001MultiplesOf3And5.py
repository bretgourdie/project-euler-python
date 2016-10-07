def sumOfMultiples(below):
  sum = 0
  for n in range(1, below):
    if n % 3 == 0 or n % 5 == 0:
      sum += n

  return sum

print("10 = " + str(sumOfMultiples(10)))
print("1000 = " + str(sumOfMultiples(1000)));
