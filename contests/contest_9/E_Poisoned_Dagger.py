test_cases = int(input())



def check(times, k, h):  
    h -= k

    for i in range(1, len(times)):
        
        if times[i] - times[i - 1] >= k:
            h -= k
        
        else:
            h -= times[i] - times[i - 1]


        if h <= 0: return True
    
    return False



def minimize_k(times, h, n):
    low = 1
    high = h
    
    best = high
    
    while low <= high:
        mid = low + (high - low) // 2

        if check(times, mid, h):
            best = mid
            high = mid - 1
        
        else:
            low = mid + 1
    
    return best





for _ in range(test_cases):
    n, h = map(int, input().split())

    times = list(map(int, input().split()))
    
    print(minimize_k(times, h, n))
