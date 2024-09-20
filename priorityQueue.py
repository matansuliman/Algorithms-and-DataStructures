import heap
import math

class MaxPriorityQueue(heap.MaxHeap):
    
    def __init__(self, arr=[]):
        heap.MaxHeap.__init__(self, arr)
    
    """
    return the max value which is in index 1
    time: O(1)
    """
    def getMax(self):
        return self._arr[1]

    """
    extract the max value from the heap array
    time: O(lgn)
    """
    def extractMax(self):
        if self._size < 1:
            print("heap underflow")
            return
        max = self._arr[1]
        self._arr[1] = self._arr[self._size]
        self._arr[self._size] = None
        self._size -= 1
        self.maxHeapifyDown(1)
        return max

    """
    increase the value in index i to key
    time: O(lgn)
    """
    def increaseKey(self, i, key):
        if key < self._arr[i]:
            print("new key is smaller than current key")
            return
        self._arr[i] = key
        while i > 1 and self._arr[self.parentIndex(i)] < self._arr[i]:
            self.swap(i, self.parentIndex(i))
            i = self.parentIndex(i)
        
    """
    insert a value to the heap and maintain its property
    time: O(lgn)
    """
    def insert(self, key):
        self._size += 1
        self._arr.append(-math.inf)
        self.increaseKey(self._size, key)


class MinPriorityQueue(heap.MinHeap):
        
    def __init__(self, arr=[]):
        heap.MinHeap.__init__(self, arr)
    
    """
    return the min value which is in index 1
    time: O(1)
    """
    def getMin(self):
        return self._arr[1]

    """
    extract the min value from the heap array
    time: O(lgn)
    """
    def extractMin(self):
        if self._size < 1:
            print("heap underflow")
            return
        max = self._arr[1]
        self._arr[1] = self._arr[self._size]
        self._arr[self._size] = None
        self._size -= 1
        self.minHeapifyDown(1)
        return max

    """
    decrease the value in index i to key
    time: O(lgn)
    """
    def decreaseKey(self, i, key):
        if key > self._arr[i]:
            print("new key is bigger than current key")
            return
        self._arr[i] = key
        while i > 1 and self._arr[self.parentIndex(i)] > self._arr[i]:
            self.swap(i, self.parentIndex(i))
            i = self.parentIndex(i)
        
    """
    insert a value to the heap and maintain its property
    time: O(lgn)
    """
    def insert(self, key):
        self._size += 1
        self._arr.append(math.inf)
        self.decreaseKey(self._size, key)