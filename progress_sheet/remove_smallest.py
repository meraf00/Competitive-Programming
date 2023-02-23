# https://codeforces.com/problemset/problem/1399/A


def check(array):
    array.sort()
    for i in range(1, len(array)):
        if abs(array[i - 1] - array[i]) > 1:
            return False
    return True
    

test_cases = int(input())

for _ in range(test_cases):
    length = input()
    array = list(map(int, input().split()))

    if check(array):
        print("YES")
    else:
        print("NO")