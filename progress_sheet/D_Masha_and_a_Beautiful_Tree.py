test_cases = int(input())


def merge(a1, a2):   
    global swap_count

    if not a1 or not a2:
        return a1 if not a2 else a2
    
    max_a1 = a1[-1]

    min_a2 = a2[0]

    if max_a1 < min_a2:
        res = a1[:]
        res.extend(a2)
        return res
    
    
    swap_count += 1
    res = a2[:]
    res.extend(a1)
    return res
    

def merge_sort(array):    
    n = len(array)

    if n <= 1:
        return array
    
    left  = merge_sort(array[:n // 2])     
    
    right = merge_sort(array[n // 2:])      

    return merge(left, right)


for _ in range(test_cases):
    size = int(input())

    nums = list(map(int, input().split()))
    
    swap_count = 0

    sorted_nums = merge_sort(nums)

    valid = True
    for i in range(1, size):
        if sorted_nums[i - 1] > sorted_nums[i]:
            valid = False
            break

    if valid:
        print(swap_count)
    
    else:
        print(-1)
