test_cases = int(input())


for _ in range(test_cases):
    sticks = list(map(int, input().split()))

    sticks.sort()
    print(sticks)
    left = 0
    right = len(sticks) - 1

    target_area = sticks[left] * sticks[right]

    while left < right:
        if sticks[left] != sticks[left + 1] or sticks[right] != sticks[right - 1] or sticks[left] * sticks[right] != target_area:
            print("NO")            
            break
            
        left += 2
        right -= 2
        
    
    print("YES")

