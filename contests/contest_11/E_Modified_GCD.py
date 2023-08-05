# https://codeforces.com/gym/437178/problem/E

from math import sqrt


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def factors(n):
    factors = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)

    if n % i == 0:
        factors.add(i)

    return factors


a, b = map(int, input().split())

gcd_ab = gcd(a, b)

n_queries = int(input())

# gcd_factors = factors(gcd_ab)
a_factors = factors(a)
b_factors = factors(b)
common_factors = sorted(a_factors.intersection(b_factors), reverse=True)

for _ in range(n_queries):
    l, h = map(int, input().split())

    if gcd_ab < l:
        print(-1)

    elif l <= gcd_ab <= h:
        print(gcd_ab)

    else:
        for factor in common_factors:
            if l <= factor <= h:
                print(factor)
                break
        else:
            print(-1)
