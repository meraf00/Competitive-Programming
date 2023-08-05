n = int(input())
nums = list(map(int, input().split()))

left = 0
removed = False
max_length = 0

marked = []

for right in range(n - 1):    

    if nums[right + 1] > nums[right]:
        length = right - left + 2 - removed
        max_length = max(length, max_length)
        continue

    elif nums[right + 1] > nums[right - 1]:        
        removed = True                
    
    else:
        marked.append(right + 1)
        left = right + 1
        removed = False
    
    length = right - left + 2 - removed
    max_length = max(length, max_length)

left = 0
current_marked = 0
for right in range(1, n):
    if current_marked >= len(marked):
        break        

    if nums[right - 1] >= nums[right] and nums[right] <= nums[marked[current_marked - 1]]:
        left = marked[current_marked]
        current_marked += 1
    
    max_length = max(max_length, right - left)
        

print(max_length)





