# https://codeforces.com/gym/438652/problem/E

import sys
from collections import defaultdict

input = sys.stdin.readline
printf = sys.stdout.write

n, m, k = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.append(0)
arr_b.append(0)

count_a = defaultdict(int)
count_b = defaultdict(int)

consecutive_count = 0
for i in range(n + 1):
    if arr_a[i] == 0:
        for j in range(consecutive_count):
            count_a[j + 1] += consecutive_count - j
        consecutive_count = 0
        continue
    consecutive_count += 1

consecutive_count = 0
for i in range(m + 1):
    if arr_b[i] == 0:
        for j in range(consecutive_count):
            count_b[j + 1] += consecutive_count - j
        consecutive_count = 0
        continue
    consecutive_count += 1


rectangle_count = 0
for width in range(1, n + 1):
    if k % width == 0:
        length = k // width
        rectangle_count += count_a[width] * count_b[length]

printf(rectangle_count)
