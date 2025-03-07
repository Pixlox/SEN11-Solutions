def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp
    return array

def smallest(array, i):
    smallest = array[i]
    pos = i
    while i < len(array):
        if array[i] < smallest:
            smallest = array[i]
            pos = i
        i += 1
    return pos

def sel_sort(array):
    i = 0
    while i < len(array):
        p = smallest(array, i)
        array = swap(array, i, p)
        i += 1
    return array


a = [5,7,9,3,4,8,6,2]
print(sel_sort(a))



