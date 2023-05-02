# https://codeforces.com/problemset/problem/1811/C

test_cases = int(input())

for _ in range(test_cases):
    original_length = int(input())

    nums = list(map(int, input().split()))

    original = [0] * original_length
    original.append(float("-inf"))
    original[0] = nums[0]

    for i in range(1, original_length):
        if max(original[i - 1], original[i]) == nums[i - 1]:
            continue

        if original[i - 2] >= nums[i - 1]:            
            original[i - 1] = nums[i - 1]

        else:
            original[i] = nums[i - 1]

    print(*original[:-1])
