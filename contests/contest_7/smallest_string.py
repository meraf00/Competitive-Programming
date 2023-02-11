from collections import Counter

test_cases = int(input())


def find_smallest(a, b, k):
    a = sorted(a)
    b = sorted(b)

    ai = 0
    bi = 0
    ak = k
    bk = k
    c = []

    while ai < len(a) and bi < len(b):

        if a[ai] <= b[bi]:
            if ak:
                c.append(a[ai])
                ai += 1
                ak -= 1
                bk = k
            else:
                c.append(b[bi])
                bi += 1
                ak = k
                bk = k - 1

        elif a[ai] > b[bi]:
            if bk:
                c.append(b[bi])
                bi += 1
                bk -= 1
                ak = k
            else:
                c.append(a[ai])
                ak = k - 1
                ai += 1
                bk = k

    return "".join(c)


for _ in range(test_cases):
    k = list(map(int, input().split()))[-1]
    a = input()
    b = input()

    print(find_smallest(a, b, k))
