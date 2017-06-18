def quick_sort(array):
    if len(array) <= 1:
        return array
    x = array[0]
    part_one = quick_sort([s for s in array[1:] if s <= x])
    part_two = quick_sort([s for s in array[1:] if not s <= x])
    return part_one + [x] + part_two
    
A = quick_sort([23, 42, 4, 16, 8, 15])
print(A)