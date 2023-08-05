from collections import Counter

test_cases = int(input())

for _ in range(test_cases):
    n_planets, machine_cost = map(int, input().split())

    planets = list(map(int, input().split()))

    count = Counter(planets)

    total_cost = 0
    for orbit, planet_count in count.items():
        if planet_count > machine_cost:
            total_cost += machine_cost

        else:
            total_cost += planet_count

    print(total_cost)
