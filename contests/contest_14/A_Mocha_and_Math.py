test_cases = int(input())

for _ in range(test_cases):
    n = int(input())

    nums = list(map(int, input().split()))

    all_and = nums[0]
    for n in nums:
        all_and = all_and & n
    
    print(all_and)