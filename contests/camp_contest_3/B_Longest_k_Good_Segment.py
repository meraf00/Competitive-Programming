n, k = map(int, input().split())

nums = list(map(int, input().split()))


seen = {}
left = 0

max_width = 0
ans = [0, 0]

for right in range(len(nums)):
    current = nums[right]

    if current in seen:
        seen[current] += 1
    else:
        seen[current] = 1

    while len(seen) > k:
        to_be_removed = nums[left]
        seen[to_be_removed] -= 1

        if seen[to_be_removed] == 0:
            del seen[to_be_removed]
        
        left += 1
    
    if right - left + 1 > max_width:
        max_width = right - left + 1
        ans[0] = left + 1
        ans[1] = right + 1

print(*ans)
    
