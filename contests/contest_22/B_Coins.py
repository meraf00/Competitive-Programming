from collections import defaultdict, deque

graph = defaultdict(list)
indegree = defaultdict(int)


for _ in range(3):
    line = input()

    a = line[0]
    op = line[1]
    b = line[2]

    if op == "<":
        graph[a].append(b)
        indegree[b] += 1

    else:
        graph[b].append(a)
        indegree[a] += 1


# toposort
queue = deque()

for key in graph:
    if indegree[key] == 0:
        queue.append(key)

order = []


while queue:
    current = queue.popleft()

    order.append(current)

    for nbr in graph[current]:
        indegree[nbr] -= 1

        if indegree[nbr] == 0:
            queue.append(nbr)

if len(order) != 3:
    print("Impossible")
else:
    print(*order, sep="")
