import math

test_cases = int(input())


for _ in range(test_cases):
    deadline, days_required = map(int, input().split())

    if deadline >= days_required:
        print("YES")
        continue
    
    low = 0
    high = deadline

    while low < high:
        mid = (low + high) // 2

        optimization_days = mid
        new_days_required = math.ceil(days_required / (optimization_days + 1))

        if new_days_required + optimization_days <= deadline:
            print("YES")
            break

        if optimization_days < new_days_required:
            low = mid + 1
        
        else:
            high = mid - 1
    
    else:
        print("NO")

        
