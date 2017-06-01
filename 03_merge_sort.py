
def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        return merge(merge_sort(array[:len(array)//2]),
                     merge_sort(array[len(array)//2:]))


def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left[0])
            left = left[1:]
        else:
            merged.append(right[0])
            right = right[1:]
    merged.extend(left + right)
    return merged

A = merge_sort([23, 42, 4, 16, 8, 15])
print(A)
