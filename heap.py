import math

class Heap:

    def __init__(self, arr=[]):
        self._arr = [None] + arr # for convenience of calculations
        self._size = len(arr)
    
    """
    return the left child index
    time: O(1)
    """
    def leftChildIndex(self, i):
        return 2*i
    
    """
    return the right child index
    time: O(1)
    """
    def rightChildIndex(self, i):
        return 2*i + 1

    """
    return the parent index
    time: O(1)
    """
    def parentIndex(self, i):
        return math.floor(i/2)

    """
    swap the values of given index in the heap array
    time: O(1)
    """
    def swap(self, i, j):
        print("swap: {} and {}".format(self._arr[i], self._arr[j]))
        temp = self._arr[i]
        self._arr[i] = self._arr[j]
        self._arr[j] = temp
    
    """
    return a readable string of the heap properties
    time: O(1)
    """
    def toString(self):
        return "heap:{} size:{}".format(self._arr[1:], self._size)

class MaxHeap(Heap):

    def __init__(self, arr=[]):
        Heap.__init__(self, arr)
        self.buildMaxHeap()

    """
    slides the value at i down the heap
    time: O(lgn)
    """
    def maxHeapifyDown(self, i):
        leftIndex = self.leftChildIndex(i)
        rightIndex = self.rightChildIndex(i)
        largestIndex = None
        # largesst = max(arr[i], arr[l], arr[r])
        if leftIndex <= self._size and self._arr[leftIndex] > self._arr[i]:
            largestIndex = leftIndex
        else: largestIndex = i
        if rightIndex <= self._size and self._arr[rightIndex] > self._arr[largestIndex]:
            largestIndex = rightIndex
        # check if need to swap
        if largestIndex != i:
            self.swap(i, largestIndex)
            self.maxHeapifyDown(largestIndex) # recursive call

    """
    constructing max heap
    max heap property: arr[parent(i)] > arr[i] for each i
    time: O(n)
    """
    def buildMaxHeap(self):
        for i in range(math.floor(self._size/2), 0, -1):
            self.maxHeapifyDown(i)

    """
    sorting the heap
    time: O(nlgn)
    
    """
    def maxHeapSort(self):
        for i in range(self._size, 1, -1):
            self.swap(1, i)
            self._size -= 1
            self.maxHeapifyDown(1)

class MinHeap(Heap):

    def __init__(self, arr=[]):
        Heap.__init__(self, arr)
        self.buildMinHeap()
    
    """
    slides the value at i down the heap
    time: O(lgn)
    """
    def MinHeapifyDown(self, i):
        leftIndex = self.leftChildIndex(i)
        rightIndex = self.rightChildIndex(i)
        largestIndex = None
        # largesst = max(arr[i], arr[l], arr[r])
        if leftIndex <= self._size and self._arr[leftIndex] < self._arr[i]:
            largestIndex = leftIndex
        else: largestIndex = i
        if rightIndex <= self._size and self._arr[rightIndex] < self._arr[largestIndex]:
            largestIndex = rightIndex
        # check if need to swap
        if largestIndex != i:
            self.swap(i, largestIndex)
            self.MinHeapifyDown(largestIndex) # recursive call

    """
    constructing min heap
    max heap property: arr[parent(i)] > arr[i] for each i
    time: O(n)
    """
    def buildMinHeap(self):
        for i in range(math.floor(self._size/2), 0, -1):
            self.MinHeapifyDown(i)