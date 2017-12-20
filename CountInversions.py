import random

def countInversions(A):
	count, _ = __countInversions(A, 0, len(A))
	return count

def __countInversions(A, start, stop):
	n = stop - start
	if n == 1:
		return 0, A[start:stop]
	countLeft, sortedLeft = __countInversions(A, start, start + n//2)
	countRight, sortedRight = __countInversions(A, start + n//2, stop)
	splitCount, sortedAll = countSplit(sortedLeft, sortedRight)
	return countLeft + countRight + splitCount, sortedAll


def countSplit(sortedLeft, sortedRight):
	sortedAll = []
	i = 0
	j = 0
	inversionsCount = 0
	while (i < len(sortedLeft) and j < len(sortedRight)):
		x = sortedLeft[i]
		y = sortedRight[j]
		if y < x:
			inversionsCount += len(sortedLeft) - i
			sortedAll.append(y)
			j += 1
		else:
			i += 1
			sortedAll.append(x)
	if i < len(sortedLeft):
		while (i < len(sortedLeft)):
			sortedAll.append(sortedLeft[i])
			i+=1
	else:
		while (j < len(sortedRight)):
			sortedAll.append(sortedRight[j])
			j+=1
	return inversionsCount, sortedAll

items = []
for i in xrange(0, 10):
	items.append(int(random.random() * 10))
print(items)
print(countInversions(items))
