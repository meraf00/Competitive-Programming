n, k = map(int, input().split())

students = list(map(int, input().split()))
students.sort()

def calculate_time(students, k):
    if k <=  len(students) // 2:
        return k * students[len(students) // 2 - 1]

    half = len(students) // 2
    time_total = half * students[half - 1]
        
    k -= half
    left = calculate_time(students[:len(students) // 2], k)
    right = calculate_time(students[len(students) // 2:], k)

    time_total += max(left, right)

    return time_total

print(calculate_time(students, k))


        