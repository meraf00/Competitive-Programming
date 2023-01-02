"""https://codeforces.com/problemset/problem/1741/A"""

from collections import Counter

def compare(tshirt1, tshirt2):
    weights = {
        "S" : -1,
        "M" : 0,
        "L" : 1
    }

    weight_1 = weights[tshirt1[-1]]
    weight_2 = weights[tshirt2[-1]]

    if weight_1 < weight_2:
        return "<"
    elif weight_1 > weight_2:
        return ">"
    
    x_count_1 = Counter(tshirt1).get("X", -1)
    x_count_2 = Counter(tshirt2).get("X", -1)

    if weight_1 * x_count_1 < weight_2 * x_count_2:
        return "<"
    elif weight_1 * x_count_1 > weight_2 * x_count_2:
        return ">"
    
    return "="

test_cases = int(input())
for _ in range(test_cases):
    line = input().split()
    t_shirt_1 = line[0]
    t_shirt_2 = line[1]

    print(compare(t_shirt_1, t_shirt_2))