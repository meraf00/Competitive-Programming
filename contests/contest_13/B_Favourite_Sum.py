test_cases = int(input())


for _ in range(test_cases):
    n, x = map(int, input().split())

    favorites = list(map(int, input().split()))

    all_sum = x * (x + 1) // 2
    
    for fav_num in favorites:
        if fav_num <= x:            
            all_sum -= 2 * fav_num
    
    print(all_sum)