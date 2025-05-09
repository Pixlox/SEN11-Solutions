def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    leftHalf = mergeSort(array[:mid])
    rightHalf = mergeSort(array[mid:])

    return merge(leftHalf, rightHalf)

def merge(left, right):
    sortedArray = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            sortedArray.append(left[leftIndex])
            leftIndex += 1
        else:
            sortedArray.append(right[rightIndex])
            rightIndex += 1

    sortedArray.extend(left[leftIndex:])
    sortedArray.extend(right[rightIndex:])

    return sortedArray

a = [5, 7, 9, 3, 4, 8, 6, 2]
b = [0, 3, 2, 4, 9, 11, 12, 10, 15, 20, 19, 26, 21, 28, 24]
c = [391, 319, 481, 4829, 318, 384, 192, 482, 3842, 4823, 586]
print(mergeSort(a))
print(mergeSort(b))
print(mergeSort(c))