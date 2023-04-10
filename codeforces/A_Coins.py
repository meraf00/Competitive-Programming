# https://codeforces.com/problemset/problem/1814/A

test_cases = int(input())

for _ in range(test_cases):
    n, k = map(int, input().split())

    if n % 2 == 0:
        print("YES")
    
    elif k % 2 == 0:
        print("NO")
    
    elif n < k:
        print("NO")
    
    else:
        print("YES")