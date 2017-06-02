from __future__ import division
import math
import operator

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        s = array[i]
        k = i
        while k > 0 and s < array[k-1]:
            array[k] = array[k-1]
            k -= 1
        array[k] = s
    return array


def bucket_sort(array):
    buckets = [[] for _ in range(10)]  # make 10 buckets
    maximum = max(array)
    minimum = min(array)
    divider = math.ceil((maximum + 1) / 10)  # take the next integer value
    for i in range(len(array)):
        bucket_index = int(math.floor(array[i]/divider))
        buckets[bucket_index].append(array[i])
    print(buckets)
    nested_sorted = map(lambda sublist: insertion_sort(sublist), buckets)
    print(nested_sorted)
    return reduce(operator.concat, nested_sorted)

A = bucket_sort([22, 45, 12, 8, 10, 6, 72, 81, 33, 18, 50, 14])
print(A)