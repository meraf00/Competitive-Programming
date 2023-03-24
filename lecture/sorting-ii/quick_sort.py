def quicksort(start, end, array):
    if start >= end:
        return
    
    pivot = array[start]
    
    write_idx = start + 1

    for read_idx in range(start + 1, end + 1):
        if array[read_idx] <= pivot:
            array[read_idx], array[write_idx] = array[write_idx], array[read_idx]
            write_idx += 1

    array[write_idx - 1], array[start] = array[start], array[write_idx - 1]

    quicksort(start, write_idx - 2, array)
    
    quicksort(write_idx, end, array)

    return array
    

def test():
    assert quicksort(0, 5, [3,0,2,-5,10,2]) == [-5,0,2,2,3,10], "Not implemented"
    assert quicksort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not implemented"
    assert quicksort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not implemented"
    assert quicksort(1, 3, [3, 2, 1, 2]) == [3, 1, 2, 2], "Not implemented"

    print("Great Job!!!")

test()