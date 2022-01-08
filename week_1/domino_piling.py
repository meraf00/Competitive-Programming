def domino_piling(m: int, n: int) -> int:
    return m * n // 2

m, n = map(int, input().split())
print(domino_piling(m, n))
