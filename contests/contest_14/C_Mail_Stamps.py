from collections import defaultdict, deque

n_stamps = int(input())

graph = defaultdict(list)

for _ in range(n_stamps):
    city_1, city_2 = map(int, input().split())

    graph[city_1].append(city_2)
    graph[city_2].append(city_1)

start = None
for k in graph.keys():
    if len(graph[k]) == 1:
        start = k
        break

queue = deque([start])
visited = set([start])

path = []

while queue:
    current = queue.popleft()

    path.append(str(current))

    for nbr in graph[current]:
        if nbr not in visited:
            queue.append(nbr)
            visited.add(nbr)

print(" ".join(path))