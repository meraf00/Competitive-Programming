# https://codeforces.com/gym/431919/problem/g


def min_operation(nums, target):
    length = len(nums)

    left = 0

    current_sum = 0

    min_operation = float("inf")

    for right in range(length):
        current_sum += nums[right]

        while left < right and current_sum > target:
            current_sum -= nums[left]
            left += 1
        
        if current_sum == target:            
            min_operation = min(length - (right - left + 1), min_operation)
    
    if min_operation == float('inf'):
        return -1
    
    return min_operation
        


test_cases = int(input())

for _ in range(test_cases):
    size, target = map(int, input().split())
    
    nums = list(map(int, input().split()))

    print(min_operation(nums, target))    