# https://codeforces.com/gym/431919/problem/f

from collections import defaultdict


def count_pairs(nums):
    seen = defaultdict(int)

    twice_average = 2 * sum(nums) / len(nums)

    count  = 0

    for num in nums:
        if twice_average - num in seen:
            count += seen[twice_average - num]
        
        seen[num] += 1
    
    return count
        


test_cases = int(input())


for _ in range(test_cases):
    size = input()

    nums = list(map(int, input().split()))

    print(count_pairs(nums))
    print()