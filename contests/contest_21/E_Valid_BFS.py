from collections import defaultdict, deque

n_nodes = int(input())

graph = defaultdict(set)

for _ in range(n_nodes - 1):
    a, b = map(int, input().split())

    graph[a].add(b)
    graph[b].add(a)

seq = list(map(int, input().split()))


queue = deque([1])

pos = 1

visited = set([1])

counter = 1

while queue:
    current = queue.popleft()

    visited.add(current)

    nbrs = set([node for node in graph if node not in visited])

    if len(nbrs.intersection(seq[pos: pos + len(nbrs)])) != len(nbrs):
        print("No")
        break

    queue.extend(seq[pos: pos + len(graph[current])])
    pos += len(graph[current])

    counter = len(graph[current])


else:
    print("Yes")
