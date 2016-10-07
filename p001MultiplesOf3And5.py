def sumOfMultiples(below):
  sum = 0
  for n in range(1, below):
    if n % 3 == 0 or n % 5 == 0:
      sum += n

  return sum

print(str(sumOfMultiples(10)))
