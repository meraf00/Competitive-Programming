# https://codeforces.com/problemset/problem/1688/A


def bit_count(n):
    count = 0
    while n:
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count


test_cases = int(input())


for _ in range(test_cases):
    n = int(input())
    
    if bit_count(n) != 1: 
        ans = 1
        while n & 1 != 1:
            n >>= 1
            ans <<= 1       
        print(ans)

    else:
        original_n = n
        shift = 1
        while n & 1 == 1:
            n >>= 1
            shift <<= 1

        ans = original_n ^ shift
    
        print(ans)