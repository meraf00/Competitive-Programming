import sys
from collections import defaultdict, deque

# input = sys.stdin.readline
# printf = sys.stdout.write

repost_count = int(input())

graph = defaultdict(list)

for _ in range(repost_count):
    dest, src = map(lambda x: x.lower().strip(), input().split(' reposted '))

    graph[src].append(dest)


queue = deque([('polycarp', 1)])
visited = set([('polycarp', 1)])

max_popularity = float('-inf')

while queue:
    current, popularity = queue.popleft()

    max_popularity = max(popularity, max_popularity)

    for nbr in graph[current]:
        if nbr not in visited:
            queue.append((nbr, popularity + 1))
            visited.add(nbr)

print(max_popularity)