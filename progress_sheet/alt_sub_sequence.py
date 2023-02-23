def max_subsequence(array):
    array_size = len(array)
    left = 0
    right = 0

    total_sum = 0
    
    while right < array_size:
        if array[left] < 0:
            max_negative = array[left]
            while right < array_size and array[right] < 0:
                max_negative = max(max_negative, array[right])
                right += 1
            total_sum += max_negative
            left = right
        else:
            max_positive = array[left]
            while right < array_size and array[right] > 0:
                max_positive = max(max_positive, array[right])
                right += 1
            total_sum += max_positive
            left = right

    return total_sum


test_cases = int(input())

for _ in range(test_cases):
    length = input()
    array = list(map(int, input().split()))

    print(max_subsequence(array))
