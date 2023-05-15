from collections import *


test_cases = int(input())

for _ in range(test_cases):
    input()

    n, k = map(int, input().split())

    graph = defaultdict(set)

    for _ in range(n - 1):
        a, b = map(int, input().split())

        graph[a].add(b)
        graph[b].add(a)
    
    queue = deque()

    for node, nbrs in graph.items():
        if len(nbrs) == 1:
            queue.append(node)
    
        
    while queue and k > 0:
        length = len(queue)

        for i in range(length):
            current = queue.popleft()                        
            
            for nbr in graph[current]:
                graph[nbr].discard(current)

                if len(graph[nbr]) == 1:
                    queue.append(nbr)
            
            graph.pop(current)
        

        
        k -= 1
    
    print(len(graph))
        


            
    

