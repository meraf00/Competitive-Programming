from collections import Counter


def isValid(b, s, c, n, rb, rs, rc, pb, ps, pc, ruble):

    deficit_b = rb - n * b
    deficit_s = rs - n * s
    deficit_c = rc - n * c
    
    if b == 0:
        deficit_b = 0
    if s == 0:
        deficit_s = 0
    if c == 0:
        deficit_c = 0
    
    if ruble + deficit_b * pb + deficit_s * ps + deficit_c * pc >= 0:
        return True
    
    return False

    
ing = input()

counter = Counter(ing)

b, s, c = counter['B'], counter["S"], counter['C']

rb, rs, rc = map(int, input().split())
pb, ps, pc = map(int, input().split())
ruble = int(input())


low = 0
high = int(max(rb // (b+.1) + ruble // pb, 
           
           rs // (s+.1) + ruble // ps, 
           
           rc // (c+.1) + ruble // pc))

while low <= high:
    mid = (low + high) // 2

    if isValid(b, s, c, mid, rb, rs, rc, pb, ps, pc, ruble):
        low = mid + 1
    
    else:
        high = mid - 1

print(high)

