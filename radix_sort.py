def radix_sort(array):
    max_len = len(str(max(array)))
    array = [str(x).zfill(max_len) for x in array]
    result = group_in_buckets(array=array,
                              digit=max_len-1)
    return [int(x) for x in result]


def group_in_buckets(array, digit):
    print(digit)
    buckets = [[] for _ in range(10)]
    for integer in array:
        get_bucket = int(integer[digit])
        buckets[get_bucket].append(integer)
    if digit > 0:
        return group_in_buckets(
                array=[integer for nest in buckets for integer in nest],
                digit=digit-1)
    elif digit == 0:
        return [integer for nest in buckets for integer in nest]

A = radix_sort([10, 15, 1, 60, 5, 100, 25, 50])
print(A)