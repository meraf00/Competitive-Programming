n, d = map(int, input().split())

players = sorted(map(int, input().split()))


counter = 0

left = 0
right = len(players) - 1

for i, p in enumerate(players):
    if p > d:
        right = i - 1
        counter = len(players) - i
        break


current_power = players[right]
while left < right:
    current_power += players[right]
    left += 1

    if current_power > d:
        counter += 1
        right -= 1
        current_power = players[right]


print(counter)
