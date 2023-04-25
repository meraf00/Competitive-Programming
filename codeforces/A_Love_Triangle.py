from collections import deque


def check_love_triange(planes):
    current = planes[0]

    seen = set()

    path = deque()

    while len(seen) < len(planes):
        if current in path and len(path) == 3:
            return True

        seen.add(current)

        path.append(current)

        if len(path) > 3:
            path.popleft()

        current = planes[current - 1]


n = input()

planes = list(map(int, input().split()))

if check_love_triange(planes):
    print("YES")

else:
    print("NO")
