import math

#Returns distance and closest pair of points in an x y plane (assumes distinct x-values)
def closestPair(points):
	pX = pointsSortedByX(points)
	pY = pointsSortedByY(points)
	return __closestPair(pX, pY)

def distance(q, r):
	return math.sqrt((q[0] - r[0])**2 + (q[1] - r[1])**2)

def __bfClosestPair(points):
	minDistance = None
	p1 = None
	p2 = None
	for i in xrange(0, len(points) - 1):
		c1 = points[i]
		for j in xrange(i+1, len(points)):
			c2 = points[j]
			d = distance(c1, c2)
			if minDistance is None or d < minDistance:
				minDistance = d
				p1 = c1
				p2 = c2
	return minDistance, p1, p2

def __closestPair(pX, pY):
	if len(pX) <= 3:
		return __bfClosestPair(pX)
	cutoffIndex = len(pX) // 2
	lX = pX[0:cutoffIndex]
	rX = pX[cutoffIndex:len(pX)]
	xCutoff = lX[len(lX)-1][0]
	lY = []
	rY = []
	for i in xrange(0, len(pY)):
		if pY[i][0] <= xCutoff:
			lY.append(pY[i])
		else:
			rY.append(pY[i])
	dL, p1Left, p2Left = __closestPair(lX, lY)
	dR, p1Right, p2Right = __closestPair(rX, rY)
	minDistance = min(dL, dR)
	p1 = None
	p2 = None
	if minDistance == dL:
		p1 = p1Left
		p2 = p2Left
	else:
		p1 = p1Right
		p2 = p2Right
	dS, p1Split, p2Split = __closestSplitPair(pX, pY, minDistance, cutoffIndex)
	if dS < minDistance:
		minDistance = dS
		p1 = p1Split
		p2 = p2Split
	return minDistance, p1, p2

def __closestSplitPair(pX, pY, minDistance, cutoffIndex):
	minX = pX[cutoffIndex][0] - minDistance
	maxX = pX[cutoffIndex-1][0] + minDistance
	sY = []
	for i in xrange(0, len(pY)):
		if minX <= pY[i][0] and pY[i][0] <= maxX:
			sY.append(pY[i])
	p1 = None
	p2 = None
	for i in xrange(0, len(sY)-1):
		c1 = sY[i]
		start = i+1
		stop = min(start+7, len(sY))
		for j in xrange(start, stop):
			c2 = sY[j]
			d = distance(c1, c2)
			if d < minDistance:
				minDistance = d
				p1 = c1
				p2 = c2
	return minDistance, p1, p2
