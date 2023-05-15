n = int(input())

for _ in range(n):
    l, r = map(int, input().split())

    if r % l == 0:
        print(l, r)
    
    else:
        print(l, l * (r // l))