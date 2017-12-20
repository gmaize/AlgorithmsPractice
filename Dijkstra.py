import random

class MinHeap():
	def __init__(self, arr=None):
		if arr is None:
			arr = []
		self.arr = arr #arr = [(itemId, heapKey), ...]
		self.itemMap = {} #map from item ids to their corresponding indices in self.arr
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

#Dijkstra's algorithm for shortest path
#returns (min distance, "min path") from source vertex to destination vertex
def getShortestPath(V, E, source, dest):
	minDistances = {} #stores the min distance from the source to each visited vertex
	minPaths = {source: str(source)} #stores the min distance path from the source to each visited vertex
	heapEntries = [(v, float('inf')) for v in V] #heap items are tuples - (vertexId, heapKey)
	minHeap = MinHeap(heapEntries) #initialize min heap with all edges infinity distance
	minHeap.decreaseKey(source, 0) #source vertex has min distance of 0
	while not minHeap.isEmpty():
		v, minDistance = minHeap.extractMin()
		minDistances[v] = minDistance
		if v == dest:
			return (minDistances[v], minPaths[v])
		for u, outgoingEdgeWeight in E[v]:
			if not minHeap.containsId(u):
				continue
			neighborMinDistance = minHeap.getHeapKey(u)
			if minDistance + outgoingEdgeWeight < neighborMinDistance:
				minPaths[u] = minPaths[v] + " " + str(u)
				minHeap.decreaseKey(u, minDistance + outgoingEdgeWeight)
