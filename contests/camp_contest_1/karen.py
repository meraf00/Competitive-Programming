n, k, q = map(int, input().split())

recommendation_count = [0] * 200002

for _ in range(n):
    low, high = map(int, input().split())
    recommendation_count[low] += 1       
    recommendation_count[high + 1] += -1

for i in range(1, 200001):
    recommendation_count[i] += recommendation_count[i - 1]

running_sum = 0
for i in range(200001):
    if recommendation_count[i] >= k:
        running_sum += 1
    
    recommendation_count[i] = running_sum

recommendation_count[-1] = 0

for _ in range(q):
    low, high = map(int, input().split())

    print(recommendation_count[high] - recommendation_count[low-1])