# https://codeforces.com/problemset/problem/9/C

def count_loaded(n, current=1, count=0):
    if current > n:
        return count

    count += 1

    for candidate in range(2):
        count = max(count_loaded(n, current * 10 + candidate, count), count)
    
    return count




n = int(input())

print(count_loaded(n))
