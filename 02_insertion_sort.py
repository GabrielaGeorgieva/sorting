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

A = insertion_sort([9, 8, 7, 3, 1, 10, 6, 5, 4, 2])
print(A)

def insertion_sort_complexity(array):
    n = len(array)
    exchanges = 0
    comparisons = 0
    for i in range(1, n):
        s = array[i]
        print('Pivot:  ', s)
        k = i
        print('k: ', k)
        while k > 0 and s < array[k-1]:
            print('move')
            comparisons += 1
            array[k] = array[k-1]
            print(array)
            k -= 1
        print('end run')
        exchanges += 1
        array[k] = s
        print(array)
    print(exchanges)
    print(comparisons)
    return array

A = insertion_sort_complexity([23, 42, 4, 16, 8, 15])
print(A)