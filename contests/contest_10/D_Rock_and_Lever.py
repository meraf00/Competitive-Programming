from collections import defaultdict

test_cases = int(input())

def rock_and_lever(arr):
    arr = list(map(lambda x: x.bit_length(), arr))

    counter = defaultdict(int)

    count = 0
    for n in arr:
        count += counter[n]
        counter[n] += 1
    
    return count
    

for _ in range(test_cases):
    length = int(input())

    nums = list(map(int, input().split()))

    print(rock_and_lever(nums))

