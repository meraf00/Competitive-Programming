# https://codeforces.com/gym/428168/problem/A

test_cases = int(input())

def sign(a):
    return 1 if a > 0 else -1

for _ in range(test_cases):
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))

    if sign(row1[0] - row2[0]) != sign(row1[1] - row2[1]) or sign(row1[0] - row1[1]) != sign(row2[0] - row2[1]):
        print("NO")
    else:
        print("YES")


