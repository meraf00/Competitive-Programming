import sys


def reverse_segment(array, left, right):
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            return False
    return True


array_size = int(input())

array = list(map(int, input().split()))
sorted_array = sorted(array)

front = 0
back = array_size - 1

while front < array_size and array[front] == sorted_array[front]:
    front += 1

while back > -1 and array[back] == sorted_array[back]:
    back -= 1

if front >= back:
    print("yes")
    print(1, 1)
    sys.exit()

reverse_segment(array, front, back)

if is_sorted(array):
    print("yes")
    print(front + 1, back + 1)  # codeforce is one indexed
    sys.exit()

print("no")
