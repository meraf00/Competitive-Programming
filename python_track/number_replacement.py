"""https://codeforces.com/problemset/problem/1744/A"""


def isValid(array, string):
    key = {}

    for num, char in zip(array, string):
        if num in key:
            if key.get(num) != char:
                return False
        else:
            key[num] = char
    return True

test_cases = int(input())

for _ in range(test_cases):
    length_of_array = int(input())
    array = list(map(int, input().split()))
    string = input()

    if isValid(array, string):
        print("YES")
    else:
        print("NO")
