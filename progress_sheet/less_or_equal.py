# https://codeforces.com/problemset/problem/977/C

n, k = map(int, input().split())
array = list(map(int, input().split()))


def check(array, k):        
    array.sort()
    if len(array) == k:
        return array[-1]

    if k == 0:
        if array[0] == 1:
            return -1
        else:
            return 1 

    for i in range(len(array) - 1):
        if array[i] != array[i+1]:
            if i+1 == k:
                return array[i]

    return -1


print(check(array, k))
