def calculate_optimal_time(ws, es, ef):
    only_walking = ws * 4
    only_elevator = (es + ef) * 4

    low = 0
    high = max(only_walking, only_elevator)

    while low <= high:
        mid = low + (high - low) // 2




    return 



test_cases = int(input())

for _ in range(test_cases):
    walk_speed, elevator_speed, elevator_floor = map(int, input().split())

    print(calculate_optimal_time(walk_speed, elevator_speed, elevator_floor))