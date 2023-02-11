n = int(input())
array = list(map(int, input().split()))

array.sort()

if sum(array[:n]) == sum(array[n:]):
    print(-1)
else:
    print(*array)