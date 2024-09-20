"""
sorts the array
prerequisites: all the numbers are from range [0, k]
stable
time: O(n + k)
"""
def countingSort(arr, k):
    result = [None] * len(arr)
    #init the counting arrayto zeros from 0 to k included
    count_array = [0] * (k+1)
    # count_array[i] containes the number on elements equal to i
    for j in range(0, len(arr)): count_array[arr[j]] += 1
    # count_array[i] containes the number on elements less than or equal to i
    for i in range(0, k+1): count_array[i] += count_array[i-1]
    #loop the elements from last to first
    for j in range(len(arr)-1, -1, -1):
        #place the elment arr[j] at the position of his count_array value
        #which represents the number of elements that are less than or equal to him
        result[count_array[arr[j]]-1] = arr[j]
        #update the counter beacuse we have placed him once now
        count_array[arr[j]] -= 1
    return result
