import sys

laptops = int(input())

price_quality_map = {}

for _ in range(laptops):
    price, quality = list(map(int, input().split()))

    price_quality_map[price] = quality

prev_quality = float("-inf")
for price in sorted(price_quality_map.keys()):
    quality = price_quality_map[price]

    if prev_quality > quality:
        print("Happy Alex")
        sys.exit()
    else:
        prev_quality = quality

print("Poor Alex")
