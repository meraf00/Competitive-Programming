test_cases = int(input())

for _ in range(test_cases):
    n_students = int(input())

    intervals = []    
    
    max_time = 0
    
    for _ in range(n_students):
        start, end = map(int, input().split())
        intervals.append((start, end))

        max_time = max(max_time, end)


    prefix = [0] * (max_time + 1)

    for start, end in intervals:
        prefix[start] += 1
        prefix[end] -= 1

    max_assistance_needed = 0
    for i in range(1, len(prefix)):
        prefix[i] += prefix[i - 1]
        max_assistance_needed = max(max_assistance_needed, prefix[i])

    print(max_assistance_needed)

