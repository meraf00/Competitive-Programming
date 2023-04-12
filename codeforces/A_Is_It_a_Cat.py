# https://codeforces.com/contest/1800/problem/A

import re

test_cases = int(input())

meow = re.compile("^[m|M]+[e|E]+[o|O]+[w|W]+$")

for _ in range(test_cases):
    input()    
    if meow.match(input()):
        print("YES")
    else:
        print("NO")
