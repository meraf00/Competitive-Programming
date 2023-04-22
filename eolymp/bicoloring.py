# https://www.eolymp.com/en/contests/30008/problems/349926


def isBipartite(graph, n_nodes):
    stack = [0]

    color = [-1] * n_nodes
    color[0] = True

    while stack:
        node = stack.pop()

        for nbr in graph[node]:
            # not visited
            if color[nbr] == -1:
                stack.append(nbr)
                color[nbr] = not color[node]

            elif color[nbr] == color[node]:
                return False

    return True


while True:
    n_nodes = int(input())

    if n_nodes == 0:
        break

    n_edges = int(input())

    graph = [[] for _ in range(n_nodes)]

    for _ in range(n_edges):
        n1, n2 = map(lambda x: int(x) - 1, input().split())

        graph[n1].append(n2)
        graph[n2].append(n1)

    if isBipartite(graph, n_nodes):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
