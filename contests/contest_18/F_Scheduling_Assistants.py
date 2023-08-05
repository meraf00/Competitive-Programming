from heapq import heappop, heappush
import sys

input = sys.stdin.readlines()

n_assistant, m_days = map(int, input[0].split())

arr = []

for i in range(n_assistant):
    start, end, available = map(int, input[i + 1].split())

    


