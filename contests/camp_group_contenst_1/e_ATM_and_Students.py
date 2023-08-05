# https://codeforces.com/gym/431919/problem/e



def max_sequence(nums, initial_amount):
    length  = len(nums)
    left    = 0

    current_amount = inital_amount

    max_length_subsequence = [1, 0]

    for right in range(length):
        current_amount += nums[right]

        while current_amount < 0:
            current_amount -= nums[left]
            left += 1

        if right - left > max_length_subsequence[1] - max_length_subsequence[0]:        
            max_length_subsequence = [left, right]        
    
    if max_length_subsequence == [1, 0]:
        return -1

    return max_length_subsequence




test_cases = int(input())


for _ in range(test_cases):
    n, inital_amount = map(int, input().split())

    nums = list(map(int, input().split()))

    
    max_seq = max_sequence(nums, inital_amount)

    if max_seq == -1:
        print(-1)
    
    else:
        print(max_seq[0] + 1, max_seq[1] + 1)


