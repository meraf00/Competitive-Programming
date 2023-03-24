def mergeSort(left, right, array):
    if left == right:
        return [array[left]]

    mid = (left + right) // 2

    left_array = mergeSort(left, mid, array)
    
    right_array = mergeSort(mid + 1, right, array)
    
    return merge(left_array, right_array)


def merge(array1, array2):    
    p1 = 0
    p2 = 0

    len_1 =  len(array1)
    len_2 =  len(array2)

    merged = []

    while p1 < len_1 and p2 < len_2:
        if array1[p1] <= array2[p2]:
            merged.append(array1[p1])
            p1 += 1
        
        else:
            merged.append(array2[p2])
            p2 += 1
            
    
    if p1 < len_1:
        merged.extend(array1[p1:])
    
    elif p2 < len_2:
        merged.extend(array2[p2:])
    
    return merged


def test():
    assert mergeSort(0, 5, [3,0,2,-5,10,2]) == [-5,0,2,2,3,10], "Not implemented"
    assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not implemented"
    assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not implemented"
    assert mergeSort(1, 3, [3, 2, 1, 2]) == [1, 2, 2], "Not implemented"

    print("Great Job!!!")

test()
