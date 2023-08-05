n, m = map(int, input().split())

rep = [i for i in range(n)]
rank = [1] * n

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
        
    if rank[repA] >= rank[repB]:
        rep[repB] = repA
        rank[repA] += rank[repB]            

    else:
        rep[repA] = repB
        rank[repB] += rank[repA]            

vertices = list(map(int, input().split()))

min_vertex_idx = float('inf')
for i in range(n):
    if vertices[i] < vertices[min_vertex_idx]:
        min_vertex_idx = i


total_cost = 0

for _ in range(m):
    x, y, cost = map(int, input().split())

    if vertices[y] + vertices[x] + 2 * vertices[min_vertex_idx] > cost + min(vertices[y], vertices[x]):
        union(x, y)
        total_cost += cost
    
    else:
        union(min_vertex_idx, )
