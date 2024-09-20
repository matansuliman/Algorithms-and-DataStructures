"""
counting sort based on a specific digit represented by exp (10^i)
"""
def counting_sort(arr, exp):
    result = [0] * len(arr) #init the counting array to zeros from 0 to k included
    count = [0] * 10
    # count[i] containes the number on elements with the log10(exp)'th digit equal to i
    for i in range(0, len(arr)):
        index = (arr[i] // exp) % 10
        count[index] += 1
    # count[i] containes the number on elements with the log10(exp)'th digit less than or equal to i
    for i in range(1, 10): count[i] += count[i - 1]
    #loop the elements from last to first
    for i in range(len(arr) - 1, -1, -1):
        #place the elment arr[j] at the position of his count_array value
        #which represents the number of elements that are less than or equal to him
        index = (arr[i] // exp) % 10
        result[count[index] - 1] = arr[i]
        #update the counter beacuse we have placed him once now
        count[index] -= 1
    #copy
    for i in range(len(arr)): arr[i] = result[i]

"""
sorting the array
prerequisits: each number is at most d digits long and one of k options per digits
time: O(d(n + k))
"""
def radix_sort(arr, d):
    # Do counting sort for every digit. exp is 10^i (i is the current digit number)
    for i in range(1, d+1):
        counting_sort(arr, pow(10,i))
