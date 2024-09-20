from numpy import random

"""
swap the values of given index in the heap array
time: O(1)
"""
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

"""
use the last element as pivot
at the end all the numbers less then or equal to the pivot are on his left,
and all the numbers grater then the pivot are on his right
time: O(n)
"""
def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, r)
    return i+1

"""
sorts the array recursivly
time: O(nlgn)
"""
def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p , q-1)
        quickSort(arr, q+1, r)

"""
use a random element as pivot
calls partition
time: O(n)
"""
def randomized_partition(arr, p, r):
    i = random.randint(p, r)
    swap(arr, i, r)
    return partition(arr, p, r)

"""
sorts the array recursivly
time: THETA(nlgn)
"""
def randomized_quickSort(arr, p, r):
    if p < r:
        q = randomized_partition(arr, p, r)
        randomized_quickSort(arr, p , q-1)
        randomized_quickSort(arr, q+1, r)
