
import random
import sys
sys.path.insert(0, '../Data Structures')
from binary_heap import BinaryHeapArray
import timeit
import copy

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

	if p1 == len(first):
		while(p2 < len(second)):
			sorted.append(second[p2])
			p2 += 1
	else:
		while(p1 < len(first)):
			sorted.append(first[p1])
			p1 += 1
	return sorted


def quickSort(items):
	start = 0
	end = len(items)
	sorted = __quickSort(items, start, end)
	return sorted

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
	return items

def __quickSortPartition(items, start, end):
	pivotIndex = end - 1
	pivot = items[pivotIndex]
	smallerTailIndex = start - 1
	unexploredIndex = start
	while unexploredIndex < pivotIndex:
		x = items[unexploredIndex]
		if x < pivot:
			smallerTailIndex += 1
			temp = items[smallerTailIndex]
			items[smallerTailIndex] = items[unexploredIndex]
			items[unexploredIndex] = temp
		unexploredIndex += 1
	items[pivotIndex] = items[smallerTailIndex + 1]
	pivotIndex = smallerTailIndex + 1
	items[pivotIndex] = pivot
	return pivotIndex

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

def heapSort(items):
	heap = BinaryHeapArray(items)
	sorted = [None] * len(items)
	i = len(items) - 1
	while not heap.isEmpty():
		max = heap.extractMax()
		sorted[i] = max
		i -= 1
	return sorted

def isSorted(items):
	for i in xrange(0, len(items)-1):
		if items[i] > items[i+1]:
			return False
	return True

def factorial(number):
	if number == 1:
		return 1
	return number * factorial(number - 1)

if __name__ == "__main__":
	nums = []
	for i in xrange(0, 50):
		x = int(random.random() * 200)
		nums.append(x)
	nums1 = copy.deepcopy(nums)
	nums2 = copy.deepcopy(nums)
	nums3 = copy.deepcopy(nums)
	print(nums3)

	start_time = timeit.default_timer()
	sorted = quickSort(nums3)
	elapsed = timeit.default_timer() - start_time
	print(isSorted(sorted))
	print("Quick Sort: " + str(elapsed))
	print(sorted)

	start_time = timeit.default_timer()
	sorted = mergeSort(nums)
	elapsed = timeit.default_timer() - start_time
	print(isSorted(sorted))
	print("Merge Sort: " + str(elapsed))
	print(sorted)


	start_time = timeit.default_timer()
	sorted = heapSort(nums1)
	elapsed = timeit.default_timer() - start_time
	print(isSorted(sorted))
	print("Heap Sort: " + str(elapsed))
	print(sorted)

#start_time = timeit.default_timer()
#	sorted = selectionSort(nums2)
#	elapsed = timeit.default_timer() - start_time
#	print(isSorted(sorted))
#	print("Selection Sort: " + str(elapsed))
