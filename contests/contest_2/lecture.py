n, k = list(map(int, input().split()))
pts = list(map(int, input().split()))
pattern = list(map(int, input().split()))

base_sum = 0
for i in range(len(pts)):
    pt = pts[i]
    awake = pattern[i]

    if awake:
        base_sum += pt
        pts[i] = 0

left = 0
right  = 0
max_k_sum = 0
while right < len(pts):
    if right - left != k:        
        max_k_sum += pts[right]
        current = max_k_sum
        right += 1        
    
    else:        
        current = current - pts[left] + pts[right]
        max_k_sum = max(current, max_k_sum)
        left += 1
        right += 1

print(base_sum + max_k_sum)
        





