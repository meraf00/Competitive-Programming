test_cases = int(input())

for _ in range(test_cases):
    nums = list(map(int, input().split()))

    minimum = min(nums)
    maximum = max(nums)

    for n in nums:
        if n != minimum and n != maximum:
            print(n)
            break
