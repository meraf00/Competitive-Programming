# https://codeforces.com/gym/431919/problem/d


from collections import defaultdict


def count_good_subarrays(nums):
    seen = defaultdict(int)

    # for num in nums:
    #     if 



test_cases = int(input())

for _ in range(test_cases):
    digits = list(map(int, list(input())))

    print(count_good_subarrays(digits))


