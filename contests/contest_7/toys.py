from collections import defaultdict

n_price_tags, n_toys = list(map(int, input().split()))
prices = list(map(int, input().split()))
prices.sort()

toys = defaultdict(int)

for _ in range(n_toys):
    toy_name = input()
    toys[toy_name] += 1


toy_count = sorted(list(toys.values()), reverse=True)

max_price = 0
min_price = 0

for index, toy_freq in enumerate(toy_count):
    min_price += prices[index] * toy_freq
    max_price += prices[n_price_tags-index-1] * toy_freq

print(min_price, max_price)
