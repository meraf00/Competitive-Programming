"""https://codeforces.com/gym/421441/problem/0"""

test_cases = int(input())

for _ in range(test_cases):
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())

    sides = set([a1, a2, b1, b2])

    if len(sides) > 3:
        print("NO")
    
    elif a1 == a2 and b1 + b2 == a1:
        print("YES")

    elif a1 == b2 and b1 + a2 == a1:
        print("YES")

    elif b1 == a2 and a1 + b2 == b1:
        print("YES")

    elif b1 == b2 and a1 + a2 == b1:
        print("YES")
    
    else:
        print("NO")
        
