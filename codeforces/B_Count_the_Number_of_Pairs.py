# https://codeforces.com/problemset/problem/1800/B

from collections import Counter


test_cases = int(input())

for _ in range(test_cases):
    n, k = map(int, input().split())

    string = input()
    counter = Counter(string)
    
    count = 0

    for char in string:    
        if char in counter and char.islower() and char.upper() in counter:
            if counter[char] < counter[char.upper()]:
                count += counter[char]
                counter[char.upper()] -= counter[char]
                del counter[char] 

            elif counter[char] > counter[char.upper()]:
                count += counter[char.upper()]
                counter[char] -= counter[char.upper()]
                del counter[char.upper()] 
            else:
                count += counter[char]
                del counter[char]
                del counter[char.upper()]
    
    
    for char in counter.keys():
        if k <= 0:
            break

        if counter[char] // 2 >= 1:            
            if k >= counter[char] // 2:
                k -= counter[char] // 2
                count += counter[char] // 2
            else:
                count += k
                k = 0
    
    print(count)

