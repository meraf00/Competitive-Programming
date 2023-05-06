# https://codeforces.com/gym/442099/my

import sys
from heapq import heapify, heappop, heappush

input = sys.stdin.readline

test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())

    boards = list(map(int, input().split()))
    ms = list(map(int, input().split()))


    
    heapify(boards)

    for n in ms:
        heappop(boards)
        heappush(boards, n)
    
    print(sum(boards))
        

