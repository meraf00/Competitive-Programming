from bisect import bisect_left


n, q = map(int, input().split())


strength = list(map(int, input().split()))
arrows   = list(map(int, input().split()))


for index in range(1, len(strength)):
    strength[index] = strength[index - 1]


front = 0
for arrow in range(len(arrows)):        
    if front >= len(arrows):        
        front = 0
        
    else:
        front = bisect_left(strength, arrow + strength[front])
    
    print(len(arrows) - front)
    