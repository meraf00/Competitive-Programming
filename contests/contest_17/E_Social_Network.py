n_users, d = map(int, input().split())

rep = [i for i in range(n_users)]
rank = [1] * n_users

max_connections = 1


def find(node):
    current = node
    while current != rep[current]:
        current = rep[current]

    while node != rep[node]:
        temp = rep[node]
        rep[node] = current
        node = temp

    return current


def union(a, b):
    global max_connections

    repA = find(a)
    repB = find(b)

    print(">>",repA,repB)
    
    if repA != repB:
        if rank[repA] >= rank[repB]:
            rep[repB] = repA
            rank[repA] += rank[repB]
            max_connections = max(rank[repA], max_connections)

        else:
            rep[repA] = repB
            rank[repB] += rank[repA]
            max_connections = max(rank[repB], max_connections)

    print(a, b, rank)
    print()


for _ in range(d):
    a, b = map(int, input().split())

    a = a - 1
    b = b - 1

    union(a, b)

    print(max_connections - 1)
