# https://codeforces.com/problemset/problem/431/C

# n - target sum
# k - number of child
# d - path must contain d
import sys

sys.setrecursionlimit(1000000007)

n, k, d = map(int, input().split())



memo = {(0, True): 1, (0, False): 0}


def counter(left_sum, contains_d):
    if (left_sum, contains_d) in memo:
        return memo[(left_sum, contains_d)]


    path_count = 0
    for i in range(1, k + 1):
        if i <= left_sum:            
            path_count += counter(left_sum - i, contains_d or i >= d)        
    
    memo[(left_sum, contains_d)] = path_count
    
    return path_count

path_count = counter(n, False)

print(path_count %  1000000007 )