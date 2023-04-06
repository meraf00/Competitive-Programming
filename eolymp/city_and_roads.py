# https://www.eolymp.com/en/contests/9060/problems/78597

n_nodes = int(input())


count = 0
for n in range(1, n_nodes + 1):
    row = list(map(int, input().split()))
    for i in range(n):
        count += row[i]

print(count)
