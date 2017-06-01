from collections import Counter
import numpy as np


def counting_sort(array):
    k = max(array)
    counting_values = [0]*(k+1)
    counter = Counter(array)
    for key in counter:
        counting_values[key] = counter[key]
    counting_values = np.cumsum(counting_values)
    print(counting_values)
    output_array = [0]*k
    for value in array:
        print('value', value)
        print('counting_values[value]', counting_values[value])
        output_array[counting_values[value]-1] = value
        counting_values[value] -= 1
    return output_array

A = counting_sort([1, 4, 1, 2, 7, 5, 2])
print(A)


