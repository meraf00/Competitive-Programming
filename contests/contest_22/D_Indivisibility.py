n = int(input())

dividers = [2, 3, 5, 7]
overcounts = [6, 10, 14, 15, 21, 35] 

count = 0
for d in dividers:
    count += n // d


for d in overcounts:
    count -= n // d

print(n - count)