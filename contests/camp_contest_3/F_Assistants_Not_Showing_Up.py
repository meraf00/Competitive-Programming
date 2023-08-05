import sys

n, m = map(int, input().split())

prefix = [0] * (n+1)

for _ in range(m):
    start, end = map(int, input().split())

    prefix[start] += 1
    prefix[end + 1] -= 1


for i in range(1, len(prefix)):
    prefix[i] += prefix[i-1]


for i in range(n):
    if prefix[i] == 0:
        print("YES")
        sys.exit()    

print("NO")

