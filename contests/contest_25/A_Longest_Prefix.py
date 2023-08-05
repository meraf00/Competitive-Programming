from collections import Counter

test_cases = int(input())

for _ in range(test_cases):
    a, b = input().split()

    counter_b = Counter(b)

    common_prefix = 0
    for letter in a:
        if letter not in counter_b or counter_b[letter] <= 0:
            break

        counter_b[letter] -= 1

        common_prefix += 1

    print(common_prefix)
