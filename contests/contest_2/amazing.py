contests = int(input())
nums = list(map(int, input().split()))

max = nums[0]
min = nums[0]
count = 0
for pt in nums[1:]:
    if pt < min:
        min = pt
        count += 1
    elif pt > max:
        max = pt
        count += 1
print(count)


