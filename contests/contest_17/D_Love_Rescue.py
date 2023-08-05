import string

rep = {c: c for c in string.ascii_lowercase}
rank = {c: 1 for c in string.ascii_lowercase}


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


n_letters = int(input())

v = input()
t = input()

for c1, c2 in zip(v, t):
    union(c1, c2)

output = []
for letter in rep.keys():
    parent = find(letter)
    if parent != letter:
        output.append(f"{letter} {parent}")

print(len(output))
print("\n".join(output))
