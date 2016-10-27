def fibValueTo(n):
	result = []
	a, b = 1, 1
	while b < n:
		result.append(b)
		a, b = b, a+b

	return result

def fibNumTo(n):
	result = []
	a, b, ii = 1, 1, 0
	while ii < n:
		result.append(b)
		a, b, ii = b, a+b, ii+1
	
	return result

