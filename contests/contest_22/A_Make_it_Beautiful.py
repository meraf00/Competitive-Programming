def check(nums):
    nums.sort()
    
    running_sum = 0

    new_order = []

    for i in range(len(nums) * 2):
        if nums[i] != running_sum:
            new_order.append(nums[i])

        running_sum += nums[i]


test_cases = int(input())

for _ in range(test_cases):
    n = input()

    nums = list(map(int, input().split()))

    if check(nums):
        print("YES")
        print(*nums)

    else:
        print("NO")
