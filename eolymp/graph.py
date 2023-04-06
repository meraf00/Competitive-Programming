# https://www.eolymp.com/en/contests/9060/problems/78602


from collections import defaultdict


graph = defaultdict(list)


def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


n_vertices = int(input())
n_instructions = int(input())
for _ in range(n_instructions):
    query = list(map(int, input().split()))

    if len(query) == 2:
        _, vertex = query
        print(*graph[vertex])

    else:
        _, u, v = query
        add_edge(graph, u, v)
