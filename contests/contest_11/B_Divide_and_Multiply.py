def div_multiply(nums):
    n_nums = len(nums)     

    largest_odd_index = 0
    
    multiply_actions = 0
    
    for i in range(n_nums):

        while nums[i] & 1 == 0:
            nums[i] //= 2
            multiply_actions += 1

        if nums[i] > nums[largest_odd_index]:
            largest_odd_index = i

    nums[largest_odd_index] *= 2 ** multiply_actions
    
    return sum(nums)


test_cases = int(input())

for _ in range(test_cases):
    input()

    nums = list(map(int, input().split()))

    print(div_multiply(nums))
