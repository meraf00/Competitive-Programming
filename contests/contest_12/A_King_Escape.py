# https://codeforces.com/gym/438652/problem/A

import sys


def sign(num):
    if num < 0:
        return -1
    return 1


input = sys.stdin.readline
printf = sys.stdout.write

dimension = int(input())

queen  = list(map(int, input().split()))
king   = list(map(int, input().split()))
target = list(map(int, input().split()))


king[0] = sign(king[0] - queen[0])
king[1] = sign(king[1] - queen[1])


target[0] = sign(target[0] - queen[0])
target[1] = sign(target[1] - queen[1])


# they are in the same quadrant when queen is considered as origin
if target == king:
    printf("YES")

else:
    print("NO")

