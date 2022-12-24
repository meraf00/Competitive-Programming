"""https://codeforces.com/gym/418150/problem/B"""

line = input()
stones = line.split()
stones = set(stones)

if len(stones) >= 5:
    print("YES")
else:
    print("NO")