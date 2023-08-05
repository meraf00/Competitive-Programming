import sys

sys.setrecursionlimit(100000000)


def isValidLefty(seq, idx):
    if idx > len(seq):
        return False

    if idx == len(seq):
        return True

    # check lefty start
    if seq[idx] < len(seq):
        return isValidLefty(seq, idx + seq[idx] + 1) or isValidRighty(seq, idx, idx)


def isValidRighty(seq, idx, last=0):
    for i in range(idx, len(seq)):
        if seq[i] == i - last:
            if isValidLefty(seq, i + 1):
                return True
    return isValidLefty(seq, idx)


test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    seq = list(map(int, input().split()))

    if isValidRighty(seq, 0):
        print("YES")
    else:
        print("NO")
