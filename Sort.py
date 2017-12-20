
def mergeSort(items):
	if len(items) <= 1:
		return items
	return __mergeSort(items, 0, len(items))

def __mergeSort(items, start, end):
	if end - start == 1:
		return [items[start]]
	mid = start + (end - start) / 2
	first = __mergeSort(items, start, mid)
	second = __mergeSort(items, mid, end)
	sorted = []
	p1 = 0
	p2 = 0
	while p1 < len(first) and p2 < len(second):
		if first[p1] <= second[p2]:
			sorted.append(first[p1])
			p1 += 1
		else:
			sorted.append(second[p2])
			p2 += 1

	#Copy uncopied items over
	while(p2 < len(second)):
		sorted.append(second[p2])
		p2 += 1
	while(p1 < len(first)):
		sorted.append(first[p1])
		p1 += 1
	return sorted


def quickSort(items):
	start = 0
	end = len(items)
	__quickSort(items, start, end)

def __quickSort(items, start, end):
	if end - start <= 1:
		return
	pivotIndex = __quickSortPartition(items, start, end) #partition
	if pivotIndex - start < end - pivotIndex + 1: #recurse on smaller half first
		__quickSort(items, start, pivotIndex)
		__quickSort(items, pivotIndex + 1, end)
	else:
		__quickSort(items, pivotIndex + 1, end)
		__quickSort(items, start, pivotIndex)

def __quickSortPartition(items, start, end):
	pivotIndex = end - 1
	pivot = items[pivotIndex]
	smallerTailIndex = start - 1
	unexploredIndex = start
	while unexploredIndex < pivotIndex:
		x = items[unexploredIndex]
		if x < pivot:
			smallerTailIndex += 1
			items[unexploredIndex] = items[smallerTailIndex]
			items[smallerTailIndex] = x
		unexploredIndex += 1
	items[pivotIndex] = items[smallerTailIndex + 1]
	items[smallerTailIndex + 1] = pivot
	return smallerTailIndex + 1

def selectionSort(itemsToSort):
	sortedList = []
	while 0 < len(itemsToSort):
		positionOfMinimum = None
		for currentPosition in xrange(0, len(itemsToSort)):
			if positionOfMinimum is None or itemsToSort[currentPosition] < itemsToSort[positionOfMinimum]:
				positionOfMinimum = currentPosition
		minimum = itemsToSort.pop(positionOfMinimum)
		sortedList.append(minimum)
	return sortedList

class BasicMaxHeap:
	def __init__(self, items):
		self.arr = items
		self.heapEnd = len(items)
		self.buildMaxHeap()

	def buildMaxHeap(self):
		for i in xrange((len(self.arr)-1)//2, -1, -1):
			self.maxHeapifyDown(i)
	
	def maxHeapifyUp(self, i):
		parentIndex = self.parentIndex(i)
		while parentIndex is not None:
			if self.arr[parentIndex] >= self.arr[i]:
				break
			temp = self.arr[parentIndex]
			self.arr[parentIndex] = self.arr[i]
			self.arr[i] = temp
			i = parentIndex
			parentIndex = self.parentIndex(i)
	
	def parentIndex(self, i):
		return (i+1) // 2 - 1 if i != 0 else None
	
	def leftChildIndex(self, i):
		leftChildIdx = i * 2 + 1
		return leftChildIdx if leftChildIdx < self.heapEnd else None
	
	def rightChildIndex(self, i):
		rightChildIdx = i * 2 + 2
		return rightChildIdx if rightChildIdx < self.heapEnd else None
	
	def maxHeapifyDown(self, i):
		max = i
		leftChildIdx = self.leftChildIndex(i)
		if leftChildIdx is None:
			return
		if self.arr[leftChildIdx] > self.arr[i]:
			max = leftChildIdx
		rightChildIdx = self.rightChildIndex(i)
		if rightChildIdx is not None and self.arr[rightChildIdx] > self.arr[i]:
			max = rightChildIdx
		if i != max:
			temp = self.arr[i]
			self.arr[i] = self.arr[max]
			self.arr[max] = temp
			self.maxHeapifyDown(max)

	def extractMax(self):
		if self.isEmpty():
			return None
		max = self.arr[0]
		self.heapEnd -= 1
		self.arr[0] = self.arr[self.heapEnd]
		self.maxHeapifyDown(0)
		return max
		

	def isEmpty(self):
		return self.heapEnd == 0

def heapSort(items):
	heap = BasicMaxHeap(items)
	sorted = [None] * len(items)
	i = len(items) - 1
	while not heap.isEmpty():
		max = heap.extractMax()
		sorted[i] = max
		i -= 1
	return sorted
