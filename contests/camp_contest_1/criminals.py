test_cases = int(input())

for _ in range(test_cases):
    n_rooms = int(input())

    rooms = list(map(int, input().split()))

    left = 0
    while left < len(rooms) and rooms[left] == 0:
        left += 1
    
    ops = 0
    for right in range(left, len(rooms)):
        if rooms[right] == 0:
            ops += 1
            rooms[right] += 1
            rooms[left] -= 1
        
        if left > len(rooms):
            break

        if rooms[left] == 0:
            left += 1   

    print(sum(rooms[:-1]) + ops)