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

left = 0
right = 1
increasing_range = []
while right < len(array):    
    if array[right] >= array[right - 1]:
        right +=1
    
    else:        
        increasing_range.append((left, right-1))
        left = right        
        right += 1

increasing_range.append((left, right-1))
if len(increasing_range) == 0:
    print("yes")
    print(left+1, right)
    sys.exit()
print(increasing_range)
for index in range(len(increasing_range) - 1):
    pass



