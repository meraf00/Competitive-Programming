import sys

test_cases = int(input())

for _ in range(test_cases):
    n_students, m_outlets = map(int, input().split())

    outlets = list(map(int, input().split()))
    outlets.sort(reverse=True)

    if n_students <= 2:
        print(0)
        continue

    available = 2    
    index = 0      
    while index < m_outlets and available < n_students:
        available += outlets[index] - 1        
        index += 1
    
    if available < n_students:
        print(-1)
    else:
        print(index)
        