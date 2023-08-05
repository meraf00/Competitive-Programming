n, c = map(int, input().split())
seconds = list(map(int, input().split()))

seconds.append(float('-inf'))


left = 0

for right in range(len(seconds) - 1):
    diff = seconds[right] - seconds[right - 1]

    if diff > c:
        left = right


print (right - left + 1)
    

