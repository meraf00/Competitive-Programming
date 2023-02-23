# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

def merge(array_1, array_2):
    ptr_1 = 0
    ptr_2 = 0
    size_1 = len(array_1)
    size_2 = len(array_2)

    merged = []
    while ptr_1 < size_1 and ptr_2 < size_2:
        if array_1[ptr_1] < array_2[ptr_2]:
            merged.append(array_1[ptr_1])
            ptr_1 += 1
        else:
            merged.append(array_2[ptr_2])
            ptr_2 += 1

    merged.extend(array_1[ptr_1:])
    merged.extend(array_2[ptr_2:])

    return merged


array_sizes = input()

array_1 = list(map(int, input().split()))
array_2 = list(map(int, input().split()))

print(*merge(array_1, array_2))

