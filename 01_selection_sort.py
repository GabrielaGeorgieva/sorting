def selection_sort(array):
    n = len(array)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


A = selection_sort([9, 8, 7, 3, 1, 10, 6, 5, 4, 2])
print(A)


def selection_sort_complexity(array):
    exchanges = 0
    comparisons = 0
    n = len(array)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                exchanges += 1
            comparisons += 1
        print("Stand nach Iteration", i, ":", array)
    print(n, "Elemente sortiert mit", exchanges,
          "Austauschen und ", comparisons, "Vergleichen")
    return array

A = selection_sort_complexity([9, 8, 7, 3, 1, 10, 6, 5, 4, 2])
print(A)


def selection_sort_divisible(array):
    exchanges = 0
    comparisons = 0
    n = len(array)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if array[i] % array[j] == 0:
                array[i], array[j] = array[j], array[i]
                exchanges += 1
            comparisons += 1
        print("Stand nach Iteration", i, ":", array)
    print(n, "Elemente sortiert mit", exchanges,
          "Austauschen und ", comparisons, "Vergleichen")
    return array

A = selection_sort_divisible([9, 8, 7, 3, 1, 10, 6, 5, 4, 2])
print(A)