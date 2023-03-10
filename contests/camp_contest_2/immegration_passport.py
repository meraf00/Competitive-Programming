import bisect

queue_length = input()

queue = input().split()

new_commers = int(input())

for _ in range(new_commers):
    name = input()
    print(bisect.bisect_left(queue, name))