# https://www.eolymp.com/en/contests/9060/problems/78605

from collections import defaultdict


def get_source_sink():
    outgoing = set()
    incoming = set()

    n_nodes = int(input())

    for node in range(n_nodes):
        row = map(int, input().split())

        for adj_node, connected in enumerate(row):
            if connected:
                outgoing.add(node + 1)
                incoming.add(adj_node + 1)

    all_nodes = set(range(1, n_nodes + 1))

    sources = all_nodes - incoming
    sinks = all_nodes - outgoing

    return sorted(sources), sorted(sinks)


sources, sinks = get_source_sink()
print(len(sources), *sources)
print(len(sinks), *sinks)
