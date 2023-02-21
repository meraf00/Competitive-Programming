n= input()

nums = list(map(int, input().split()))
nums.sort()
left = 0
right = 1
m = 1
while right < len(nums):
    if nums[right] - nums[left] > 5:
        m = max(m, right-left)
        left += 1
     
    right += 1
m = max(m, right-left)
print(m)