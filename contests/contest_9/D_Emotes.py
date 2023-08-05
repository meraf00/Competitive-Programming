n, m, k = map(int, input().split())


emotes = list(map(int, input().split()))

emotes.sort()

largest = emotes[-1]
second_largest = emotes[-2]

groups = m // (k + 1) 

total = groups * (k * largest + second_largest) + (m % (k+1)) * largest

print(total)


