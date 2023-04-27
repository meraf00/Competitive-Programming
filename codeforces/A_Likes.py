# https://codeforces.com/problemset/problem/1802/A


import sys

input = sys.stdin.readline
printf = sys.stdout.write

test_cases = int(input())


for _ in range(test_cases):
    n = int(input())

    actions = map(int, input().split())

    negative_count = 0
    positive_count = 0

    for act in actions:
        if act < 0:
            negative_count += 1

        elif act > 0:
            positive_count += 1

    max_likes = [0] * n
    min_likes = [0] * n

    for i in range(positive_count):
        max_likes[i] = i + 1

    for i in range(positive_count, n):
        max_likes[i] = max_likes[i - 1] - 1

    for i in range(0, negative_count * 2, 2):
        min_likes[i] = 1
        min_likes[i + 1] = 0

    for i in range(negative_count * 2, n):
        min_likes[i] = i - negative_count * 2 + 1

    printf(" ".join(map(str, max_likes)))
    printf("\n")
    printf(" ".join(map(str, min_likes)))
    printf("\n")
