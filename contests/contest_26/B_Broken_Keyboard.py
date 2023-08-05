

test_cases = int(input())


for _ in range(test_cases):
    line = input() + ' '

    left = 0
    working = set()
    for right, char in enumerate(line):
        if char != line[left]:
            # if odd
            if (right - left) & 1:
                working.add(line[left])
            left = right

    print(*sorted(working), sep='')
