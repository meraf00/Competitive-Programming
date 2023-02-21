n= input()

nums = list(map(int, input().split()))

left = 0
right = 1
m = 1
while right < len(nums):
    if nums[right - 1] > nums[right]:
        m = max(m, right-left)
        left = right
     
    right += 1
m = max(m, right-left)
print(m)