import math
import sys

MOD = 10 ** 9 + 7

input()

lines = sys.stdin.readlines()

ans = []
for line in lines:
    a, b = map(int, line.strip().split())

    if b >= a:
        ans.append("0")
        continue

    total_changes_available = (a - 1) 

    if total_changes_available - b > 0:
        b = min(b, total_changes_available - b)

    ans.append(str((math.comb(total_changes_available, b) * 2) % MOD))

print("\n".join(ans))
    
"""
7
2 1
4 3
2 0
3 0
3 1
3 2
3 3
4 0
4 1
4 2
4 3
4 4
5 0
5 1
5 2
5 3
5 4
5 5
"""