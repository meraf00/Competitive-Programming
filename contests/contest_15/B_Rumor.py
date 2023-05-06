import sys
from collections import *


input = sys.stdin.readline
printf = sys.stdout.write


def bfs(graph, start, visited, golds):
    queue = deque([start])

    min_cost = float('inf')
    while queue:
        curr = queue.popleft()

        if golds[curr] < min_cost:
            min_cost = golds[curr]

        for nbr in graph[curr]:
            if nbr not in visited:
                visited.add(nbr)                
                queue.append(nbr)
    
    return min_cost


n_chars, friend_pairs = map(int, input().split())

golds = list(map(int, input().split()))


graph = defaultdict(list)

for _ in range(friend_pairs):
    a, b = map(int, input().split())

    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visited = set()
total_cost = 0
for char in range(n_chars):
    if char not in visited:
        total_cost += bfs(graph, char, visited, golds)

printf(f"{total_cost}\n")
