"""https://codeforces.com/problemset/problem/1730/A"""


from collections import defaultdict

def minimizeCost(planets, c):
    orbit = defaultdict(int)

    for planet in planets:
        orbit[planet] += 1
    
    total_cost = 0

    for num_of_planets in orbit.values():
        if num_of_planets < c:
            total_cost += num_of_planets
        else:
            total_cost += c
    
    return total_cost


test_cases = int(input())
for _ in range(test_cases):
    number_of_planets, c = list(map(int, input().split()))
    planets = list(map(int, input().split()))

    print(minimizeCost(planets, c))
