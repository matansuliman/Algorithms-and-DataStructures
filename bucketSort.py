import math

"""
sorting the array
prerequisits: all numbers are evenly distributed on [0,1)
time: O(n)
"""
def bucket_sort(arr):
    # create empty buckets
    bucket_count = len(arr)
    buckets = [[] for i in range(bucket_count)]
    # put array elements into buckets
    for num in arr:
        index = math.floor(num * bucket_count)  # Bucket index for the element
        buckets[index].append(num)
    # sort all buckets
    for i in range(bucket_count):
        buckets[i].sort()
    # concatenate all buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    return sorted_arr
