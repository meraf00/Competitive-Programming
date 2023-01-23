import sys
array_size = int(input())

array  = list(map(int, input().split()))

array.sort()

for i in range(array_size * 2):
    i = i % array_size
    if array[i] >= array[i-1] + array[(i+1) % array_size]:
        print("NO")
        sys.exit()

print("YES")
print(" ".join(map(str, array)))