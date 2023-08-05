from collections import deque


def check_triangle(start, graph, visited):

    path = []

    current = start

    while True:
        path.append(current)
        visited.add(current)

        nbr = graph[current]

        if nbr in visited:
            if len(path) >= 3 and path[-3] == nbr:
                return True
            else:
                return False

        current = nbr


def check_love_triange(planes):
    n_planes = len(planes)
    graph = {}

    visited = set()

    for i in range(n_planes):
        graph[i + 1] = planes[i]

    for node in graph:
        if node in visited:
            continue

        if check_triangle(node, graph, visited):
            return True

    return False


n = input()

planes = list(map(int, input().split()))

if check_love_triange(planes):
    print("YES")

else:
    print("NO")
