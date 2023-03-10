from collections import defaultdict

n, a, b = map(int, input().split())

students = list(map(int, input().split()))

allowed = range(a, b + 1)

for i in range(1, len(students)):
    students[i] += students[i - 1]

students.append(0)

sub_arrays = 0

counter = defaultdict(int)

left = 0

for right, solved in enumerate(students):
    current_sum = students[right] - students[left - 1]
        
    
    while current_sum > b:
        current_sum -= students[left]
        left += 1

    if current_sum in allowed:
        sub_arrays += 1

    for other, count in counter.items():
        if (current_sum - other) in allowed:
            sub_arrays += count                
    
    counter[current_sum] += 1


print(sub_arrays)
        


