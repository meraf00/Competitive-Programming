# https://www.eolymp.com/en/contests/9060/problems/78605

from collections import defaultdict


graph = defaultdict(list)

n_nodes = int(input())


for node in range(n_nodes):
    row = map(int, input().split())

    for adj_node, connected in enumerate(row):
        if connected:
            graph[node + 1].append(adj_node + 1)


for node in range(n_nodes):
    adj = graph[node + 1]
    print(len(adj), *sorted(adj))
