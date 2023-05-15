from collections import *
import sys

n, m = map(int, input().split())

graph = defaultdict(list)

directions = []

for _ in range(m):
    a, b = map(int, input().split())

    directions.append((a, b))

    graph[a].append(b)
    graph[b].append(a)


colors = [-1] * n

start = list(graph.keys())[0] 

colors[start - 1] = True

queue = deque([start])

while queue:
    current = queue.popleft()
    
    current_color = colors[current - 1]

    for nbr in graph[current]:        
        if colors[nbr - 1] == current_color:
            print("NO")
            sys.exit()

        if colors[nbr - 1] == -1:            
            colors[nbr - 1] = not current_color
            queue.append(nbr)

print("YES")
for i, edge in enumerate(directions):
    a, b = edge
    if colors[a - 1]:
        directions[i] = "1"
    else:
        directions[i] = "0"
print(*directions, sep="")

