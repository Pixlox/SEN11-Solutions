def quickSort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]

    return quickSort(less) + equal + quickSort(greater)

a = [5, 7, 9, 3, 4, 8, 6, 2]
b = [0, 3, 2, 4, 9, 11, 12, 10, 15, 20, 19, 26, 21, 28, 24]
c = [391, 319, 481, 4829, 318, 384, 192, 482, 3842, 4823, 586]
print(quickSort(a))
print(quickSort(b))
print(quickSort(c))