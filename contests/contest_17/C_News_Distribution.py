import sys

inp = list(sys.stdin)


n_users, m_groups = map(int, inp[0].split())

rep = [i for i in range(n_users)]
rank = [1] * n_users


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
    repA = find(a)
    repB = find(b)

    if repA == repB:
        return

    if rank[repA] >= rank[repB]:
        rep[repB] = repA
        rank[repA] += rank[repB]

    else:
        rep[repA] = repB
        rank[repB] += rank[repA]


for grp in range(m_groups):
    info = list(map(int, inp[grp + 1].split()))

    count = info[0]

    if count == 0:
        continue

    x = info[1] - 1

    for i in range(2, len(info)):
        union(x, info[i] - 1)


users = [0] * n_users
for user in range(n_users):
    users[user] = rank[find(user)]

print(*users)
