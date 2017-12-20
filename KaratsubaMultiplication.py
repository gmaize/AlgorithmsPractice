
def karatsubaMultiply(x, y):
	if x == 0 or y == 0:
		return 0
	elif x == 1:
		return y
	elif y == 1:
		return x
	strX = str(x)
	strY = str(y)
	n = max(len(strX), len(strY))
	if n == 1:
		return x * y
	nby2 = n // 2
	denom = 10 ** nby2
	a = x // denom
	b = x % denom
	c = y // denom
	d = y % denom
	ac = karatsubaMultiply(a, c)
	bd = karatsubaMultiply(b, d)

	crossProduct = karatsubaMultiply((a+b), (c+d))
	midterm = crossProduct - ac - bd
	return (10**(2*nby2)*ac) + (10**nby2) * midterm + bd

result = karatsubaMultiply(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
print(result)
