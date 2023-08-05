from collections import defaultdict, Counter
from heapq import heappush

test_cases = int(input())


for _ in range(test_cases):

    degree_graph = defaultdict(int)    

    n, m = map(int, input().split())

    for _ in range(m):
        a, b = map(int, input().split())

        degree_graph[a] += 1
        degree_graph[b] += 1
    
    degrees = Counter(degree_graph.values())
    degrees.pop(1)    
    
    
    arr = []
    for k, v in degrees.items():
        heappush(arr, (v, k))
    
    
    if len(arr) == 1:
        x = arr[0][1]
        y = x - 1
    else:
        x = arr[0][1]
        y = arr[1][1] - 1
    
    print(x, y)