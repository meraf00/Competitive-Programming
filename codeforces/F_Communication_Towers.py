from collections import defaultdict, deque


def bfs(graph, acceptable_freq):
    stack = [(1, acceptable_freq[1])]

    visited = set()

    reachable_nodes = set()

    while stack:
        current, passed_freq = stack.pop()

        visited.add((current, passed_freq))

        reachable_nodes.add(current)

        for nbr in graph[current]:
            nbr_l, nbr_h = acceptable_freq[nbr]

            allowed_freq = (max(passed_freq[0], nbr_l), min(
                passed_freq[1], nbr_h))

            if (nbr, allowed_freq) not in visited:
                if allowed_freq[0] <= allowed_freq[1]:
                    stack.append((nbr, allowed_freq))

    return sorted(reachable_nodes)


n, m = map(int, input().split())

acceptable_freq = {}

graph = defaultdict(list)

for tower in range(n):
    low, high = map(int, input().split())

    acceptable_freq[tower + 1] = (low, high)

for _ in range(m):
    tower_1, tower_2 = map(int, input().split())

    graph[tower_1].append(tower_2)
    graph[tower_2].append(tower_1)


reachable = bfs(graph, acceptable_freq)
print(*reachable)
