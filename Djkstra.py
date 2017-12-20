import random

class MinHeap():
	def __init__(self, arr=[]):
		#arr is array of tuples
		self.arr = arr
		self.itemMap = {}
		self.numItems = len(arr)
		if len(arr) != 0:
			self.buildItemMap()
			self.buildMinHeap()

	def containsId(self, id):
		return id in self.itemMap

	def isEmpty(self):
		return self.numItems == 0
	
	def buildItemMap(self):
		for i in xrange(0, self.numItems):
			item = self.arr[i]
			self.itemMap[item[0]] = i

	def __swap(self, i, j):
		temp = self.arr[i]
		self.arr[i] = self.arr[j]
		id1 = self.arr[i][0]
		self.itemMap[id1] = i
		self.arr[j] = temp
		id2 = temp[0]
		self.itemMap[id2] = j
	
	def getHeapKey(self, id):
		idx = self.itemMap[id]
		return self.arr[idx][1]

	def insertItem(self, id, heapKey):
		if self.numItems < len(self.arr):
			self.arr[self.numItems] = (id, heapKey)
		else:
			self.arr.append((id, heapKey))
		self.itemMap[id] = self.numItems
		self.numItems += 1
		self.minHeapifyUp(self.numItems - 1)

	def parentIndex(self, i):
		return (i+1)//2 - 1 if i != 0 else None

	def leftChildIndex(self, i):
		left = i * 2 + 1
		return left if left < self.numItems else None

	def rightChildIndex(self, i):
		right = i * 2 + 2
		return right if right < self.numItems else None

	def minHeapifyUp(self, i):
		parentIndex = self.parentIndex(i)
		while parentIndex is not None and self.arr[i][1] < self.arr[parentIndex][1]:
			self.__swap(parentIndex, i)
			i = parentIndex
			parentIndex = self.parentIndex(i)

	def extractMin(self):
		if self.isEmpty():
			return None
		min = self.arr[0]
		self.__swap(0, self.numItems - 1)
		self.itemMap.pop(min[0], None)
		self.numItems -= 1
		self.minHeapifyDown(0)
		return min
			
	def decreaseKey(self, id, newHeapKey):
		idx = self.itemMap[id]
		item = self.arr[idx]
		self.arr[idx] = (item[0], newHeapKey)
		self.minHeapifyUp(idx)

	def minHeapifyDown(self, i):
		while True:
			leftChildIndex = self.leftChildIndex(i)
			if leftChildIndex is None:
				break
			min = i
			if self.arr[leftChildIndex][1] < self.arr[min][1]:
				min = leftChildIndex
			rightChildIndex = self.rightChildIndex(i)
			if rightChildIndex is not None and self.arr[rightChildIndex][1] < self.arr[min][1]:
				min = rightChildIndex
			if min == i:
				break
			self.__swap(i, min)
			i = min

	def buildMinHeap(self):
		for i in xrange(self.numItems//2 - 1, -1, -1):
			self.minHeapifyDown(i)

	def printHeap(self):
		print(self.arr)


def verifyShortestPath(E, source, dest):
	partialPaths = {}
	__verifyShortestPath(E, source, dest, set(), partialPaths)
	if len(partialPaths[source]) == 0:
		print("No Path Found")
	else:
		for path, dist in sorted(partialPaths[source], key=lambda tup: tup[1]):
			print(str(dist) + ": " + path)

def __verifyShortestPath(E, curSource, dest, currentlyVisited, partialPaths):
	if curSource == dest:
		partialPaths[curSource] = [(str(curSource), 0)]
		return
	if curSource in partialPaths:
		return
	partialPaths[curSource] = []
	currentlyVisited.add(curSource)
	for u, edgeWeight in E[curSource]:
		if u in currentlyVisited:
			continue
		__verifyShortestPath(E, u, dest, currentlyVisited, partialPaths)
		for partialPathFromSibling, distOfPartialPathFromSibling in partialPaths[u]:
			newPartialPath = str(curSource) + " " + partialPathFromSibling
			newPartialPathDist = edgeWeight + distOfPartialPathFromSibling
			partialPaths[curSource].append((newPartialPath, newPartialPathDist))
	currentlyVisited.remove(curSource)



#heap items are tuples - (key, value, id)
#random graph
V = list(range(0, 1000))
items = [(v, float('inf')) for v in V]
E = {}
for v in V:
	E[v] = []
	potentialDests = [dest for dest in V if dest != v]
	numEdges = int(random.random()*len(V)//2)
	for i in xrange(0, numEdges):
		j = int(random.random() * len(potentialDests))
		u = potentialDests.pop(j)
		E[v].append((u, int(random.random()*100)))


#dijkstra's
D = {}
heap = MinHeap(items) #initialize min heap with all edges infinity distance
s = 0 #source vertex
dest = 4 #destination vertex
paths = {0: "0"}
heap.decreaseKey(s, 0) #source path has score of 0
while not heap.isEmpty(): #while min heap is not empty (nodes left to compute shortest path)
	v, d = heap.extractMin() # remove min path node
	D[v] = d
	if v == dest:
		break
	for u, w in E[v]:
		if not heap.containsId(u):
			continue
		prevDistance = heap.getHeapKey(u)
		if d + w < prevDistance:
			paths[u] = paths[v] + " " + str(u)
			heap.decreaseKey(u, d + w)

print("")
print("Source: "+str(s))
print("Dest: "+ str(dest))
print("")
print("Dijkstra:")
path = paths[dest] if dest in paths else "NONE"
print(str(D[dest])+": "+path)
print("")
#verifyShortestPath(E, s, dest)
print("")
