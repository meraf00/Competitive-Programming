n, k = map(int, input().split())

length = []
beauty = []

lb = []

for idx in range(n):
    l, b = map(int, input().split())

    length.append(l)
    beauty.append(b)

    lb.append((l, b, idx, l * b))


lb.sort(key=lambda v: v[-1])

length_sum = 0
min_beauty = float('inf')
for l, b, idx, lb in lb[-k:]:
    length_sum += l
    min_beauty = min(min_beauty, b)

print(length_sum * min_beauty)



