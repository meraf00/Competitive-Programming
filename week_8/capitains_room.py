"""https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())
rooms = map(int, input().split(" "))

counter = {}

for room in rooms:
    if counter.get(room):
        counter[room] += 1
    else:
        counter[room] = 1

for rc in counter.items():
    if rc[1] == 1:
        print(rc[0])
        break
