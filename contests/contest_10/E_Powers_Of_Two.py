from heapq import heappop, heappush, heapify

def check(n, k):
    if k > n:
        return
    
    index = 0
    power_of_twos = []

    while n:
        if n & 1:
            power_of_twos.append(1 << index)
        
        index += 1 
        n >>= 1
    
    for i in range(len(power_of_twos)):        
        power_of_twos[i] *= -1

    heapify(power_of_twos)
    while len(power_of_twos) < k:
        max_power_of_2 = -1 * heappop(power_of_twos)
        heappush(power_of_twos, -1 * max_power_of_2 // 2)
        heappush(power_of_twos, -1 * max_power_of_2 // 2)

    if len(power_of_twos) > k:
        return
    
    for i in range(len(power_of_twos)):        
        power_of_twos[i] *= -1

    return sorted(power_of_twos)



n, k = map(int, input().split())

val = check(n, k)

if not val:
    print("NO")

else:
    print("YES")
    print(*val)
