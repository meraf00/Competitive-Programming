from itertools import combinations
from collections import defaultdict
import sys

n, k = map(int, input().split())

people = []

for _ in range(n):
    people.append(input())


graph = defaultdict(set)

for _ in range(k):
    a, b = input().split()
    
    graph[a].add(b)
    graph[b].add(a)


def check(combination):
    for person in combination:
        if len(combination.intersection(graph[person])) != 0:
            return False
    return True

groups = []

for i in range(1, len(people) + 1):
    groups.extend(combinations(people, i))

ans = []
for comb in map(set, groups):
    if check(comb) and len(ans) < len(comb):
        ans = comb

print(len(ans))
print("\n".join(sorted(ans)))
        
        