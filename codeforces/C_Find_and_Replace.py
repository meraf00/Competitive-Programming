# https://codeforces.com/problemset/problem/1807/C

import sys

printf = sys.stdout.write

test_cases = int(input())

for _ in range(test_cases):
    input()

    word = input()

    word_map = {}

    last = True
    for char in word:
        if char not in word_map:
            word_map[char] = not last

        elif word_map[char] == last:
            printf("NO\n")
            break

        last = not last

    else:
        printf("YES\n")
