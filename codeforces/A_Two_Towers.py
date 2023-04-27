# https://codeforces.com/problemset/problem/1795/A

import sys


input = sys.stdin.readline
printf = sys.stdout.write


def is_possible(first_tower, second_tower):
    # color, tower status upto this block
    first_tower[0] = (first_tower[0], True)

    # color, tower status upto this block
    second_tower[0] = (second_tower[0], True)

    for i in range(1, len(first_tower)):
        color, status = first_tower[i - 1]

        if first_tower[i] == color:
            first_tower[i] = (color, False)
        else:
            first_tower[i] = (first_tower[i], status and True)

    for i in range(1, len(second_tower)):
        color, status = second_tower[i - 1]

        if second_tower[i] == color:
            second_tower[i] = (color, False)
        else:
            second_tower[i] = (second_tower[i], status and True)

    possible = first_tower[-1][1] and second_tower[-1][1]

    def backtrack():
        nonlocal possible

        if first_tower[-1][1] and second_tower[-1][1]:
            possible = True
            return possible

        if not possible and first_tower[-1][0] == second_tower[-1][0]:
            return False

        both_not_beautiful = not (first_tower[-1][1] or second_tower[-1][1])

        if both_not_beautiful:
            possible = False
            return False

        if len(second_tower) > 1 and second_tower[-1][1] == False:
            color, state = second_tower.pop()
            first_tower.append((color, True))
            backtrack()
            second_tower.append((color, state))

        if len(first_tower) > 1 and first_tower[-1][1] == False:
            color, state = first_tower.pop()
            second_tower.append((color, True))
            backtrack()
            first_tower.append((color, state))

    backtrack()

    return possible


test_cases = int(input())


for _ in range(test_cases):
    n, m = map(int, input().split())

    first_tower = list(input().strip())
    second_tower = list(input().strip())

    if is_possible(first_tower, second_tower):
        printf("YES\n")

    else:
        printf("NO\n")
