import sys
from collections import *
from heapq import heapify, heappop, heappush


input = sys.stdin.readline


test_cases = int(input())

for _ in range(test_cases):
    n_people = int(input())

    sociability_ = map(lambda x: -int(x) , input().split())
    
    sociability = []    
    for i, s in enumerate(sociability_):
        if s != 0:
            sociability.append((s, i))
            i += 1 


    heapify(sociability)

    n_talks = 0
    
    people = []
    
    while len(sociability) >= 2:        
        max_soc, idx1 = heappop(sociability)
        
        second_max_soc, idx2 = heappop(sociability)

        max_soc *= -1
        second_max_soc *= -1

        n_talks += 1

        max_soc -= 1
        second_max_soc -= 1

        if max_soc:
            heappush(sociability, (-max_soc, idx1))
        
        if second_max_soc:
            heappush(sociability, (-second_max_soc, idx2))
        
        people.append(f"{idx1 + 1} {idx2 + 1}")
    
    print(n_talks)
    if n_talks:
        print("\n".join(people))    
    
    
