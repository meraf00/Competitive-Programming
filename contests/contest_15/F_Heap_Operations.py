from heapq import heapify, heappop, heappush, heappushpop

n_ops = int(input())

heap = []
log = []

for _ in range(n_ops):
    instruction = input()

    if instruction == 'removeMin':
        if not heap:
            log.append("insert 0")           

        else:
            heappop(heap)
        log.append('removeMin')
    
    elif instruction.startswith("insert"):
        n = int(instruction.split()[1])
        heappush(heap, n)
        log.append(f"insert {n}")
    
    elif instruction.startswith("getMin"):
        n = int(instruction.split()[1])
        
        if not heap:            
            heappush(heap, n)
            log.append(f"insert {n}")
            log.append(f"getMin {n}")
                    
        elif heap[0] == n:            
            log.append(f"getMin {n}")
        
        elif heap[0] > n:
            heappush(heap, n)
            log.append(f"insert {n}")
            log.append(f"getMin {n}")
        
        else:
            while heap and heap[0] < n:
                heappop(heap)
                log.append("removeMin")
            
            if heap and heap[0] == n:                             
                log.append(f"getMin {n}")
            else:
                heappush(heap, n)
                log.append(f"insert {n}")
                log.append(f"getMin {n}")

print(len(log))
print("\n".join(log))


            


