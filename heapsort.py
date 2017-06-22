"""
For a given array let:

        Parent(i)=floor(i/2)
        Left(i)=2i
        Right(i)=2i+1

    An array has the max heap property if:
        array[ Parent(i) ] >= array[ i ]

    We also say that the corresponding binary tree is a Max Heap

    Notes:
        --> In a Max Heap array A the element with the highest
        value is in the root

        --> The values of the elements lying on a root-leave-path
        are monotonically decreasing

        --> The height of the tree of the tree i.e.
        length of the longest root-leave-path is floor(log(n))

"""


def max_heapify(array, root):
    """
    Restore max heap property in the i-th element

    :param array: list
    :param i: integer
    :return:
    """
    print(array)
    while True:
        left_child = 2*i
        right_child = 2*i + 1
        print(left_child, right_child)
    n = len(array)

    if left_child <= n and array[left_child] > array[i]:
        largest = left_child
    else:
        largest = i
    print(right_child)
    print('largest index',largest)
    if right_child <= n and array[right_child] > array[largest]:
        largest = right_child
    print(array[largest])

    if largest != i:
        a, b = array.index(array[i]), array.index(array[largest])
        array[b], array[a] = array[a], array[b]
        print(largest)
        return max_heapify(array, largest)

print(max_heapify([1, 2, 3, 4, 5], 0))

