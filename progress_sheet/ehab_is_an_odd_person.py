# https://codeforces.com/problemset/problem/1174/B

size = input()

array = list(map(int, input().split()))

odd = False
even = False
for num in array:
    if odd and even:
        break

    if num % 2:
        odd = True
    else:
        even = True

if odd and even:
    array.sort()
    print(*array)
else:
    print(*array)