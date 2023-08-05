from collections import defaultdict


def build(array):
    graph = defaultdict(list)
    root = None

    for i in range(len(array)):
        child = i + 1
        parent = array[i]

        if child != parent:
            graph[parent].append(child)

        if child == parent:
            root = child

    return graph, root


test_cases = int(input())

for _ in range(test_cases):
    input()

    array = list(map(int, input().split()))

    tree, root = build(array)    

    # dfs
    stack = [root]
    visited = set([0]) 
    paths = []    
    current_path = defaultdict(int)
    current_path[root] = 0

    while stack:           
        node = stack.pop()    
        
        if tree[node] == []: 
            path = [node]                
            while current_path[node] not in visited:                
                visited.add(current_path[node])                
                path.append(current_path[node])
                node = current_path[node]
            paths.append(list(reversed(path)))           
            
            continue

        for child in tree[node]:                                   
            stack.append(child)
            current_path[child] = node
                

    print(len(paths))
    for path in paths:
        print(len(path))
        print(*path)
    print()
    
