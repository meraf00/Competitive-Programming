n, k = map(int, input().split())

ratings = list(map(int, input().split()))

for i in range(len(ratings)):
    ratings[i] = (ratings[i], i)


def merge_sort(arr, left, right):    
    if left == right:
        return [arr[left]]
    
    mid = (left + right) // 2

    left_arr = merge_sort(arr, left, mid)
    right_arr = merge_sort(arr, mid + 1, right)

    return merge(left_arr, right_arr)


def merge(arr_1, arr_2):
    p1 = 0
    p2 = 0

    l1 = len(arr_1)
    l2 = len(arr_2)

    merged = []

    while p1 < l1 and p2 < l2:        
        if arr_1[p1][0] <= arr_2[p2][0]: 
            if arr_2[p2][0] - arr_1[p1][0] <= k:
                merged.append(arr_1[p1])
            p1 += 1
        
        else:
            if arr_1[p1][0] - arr_2[p2][0] <= k:
                merged.append(arr_2[p2])
            p2 += 1
        

    merged.extend(arr_1[p1:])
    merged.extend(arr_2[p2:])

    return merged

possible_winners = map(lambda x: x[1] + 1, merge_sort(ratings, 0, len(ratings) - 1))
print(*sorted(possible_winners))