import sys


n = int(input())
m = int(input())

benches = []
for _ in range(n):
    benches.append(int(input()))


benches.sort()

max_k = benches[-1] + m

min_k = benches[0]


for i in range(len(benches) - 1):
    deficit = benches[i + 1] - benches[i]

    if deficit != 0:
        left = m - deficit * (i + 1)
        m = m - left
        min_k = min_k + (m // (i + 1) + ((m % (i + 1)) != 0))
        m = left
    
    if m <= 0:
        break


if m > 0:
    min_k = min_k + (m // len(benches) + ((m % len(benches)) != 0))

print(min_k, max_k)
