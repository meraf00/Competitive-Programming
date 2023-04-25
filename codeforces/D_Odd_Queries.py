import sys

input = sys.stdin.readline

test_cases = int(input())

for _ in range(test_cases):
    n, q = map(int, input().split())

    nums = [0]
    nums.extend(map(int, input().split()))
    # prefix sum
    for i in range(1, n + 1):
        nums[i] += nums[i - 1]    
    
    total_sum = nums[-1]

    for _ in range(q):
        left, right, k = map(int, input().split())

        # sum_after_right = nums[-1] - nums[right]

        # sum_before_left = nums[left - 1]        

        # removed_count = right - left + 1

        # new_sum = sum_before_left + sum_after_right + k * removed_count

        new_sum = nums[left - 1] + total_sum - nums[right] + k * (right - left + 1)

        if new_sum %  2 != 0:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
