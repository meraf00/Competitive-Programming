n_boys = int(input())
boys = list(map(int, input().split()))

n_girls = int(input())
girls = list(map(int, input().split()))

boys.sort()
girls.sort()

b = 0
g = 0

pair_count = 0
while b < n_boys and g < n_girls:
    if abs(boys[b] - girls[g]) <= 1:
        pair_count += 1
        b += 1
        g += 1
    elif boys[b] < girls[g]:
        b += 1
    
    else:
        g += 1

print(pair_count)