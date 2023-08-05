def calc(left, right):
    lower = left.bit_length()
    upper = right.bit_length()

    if left == right:
        return 0

    elif lower == upper:
        i = 0
        for l, r in zip(bin(left), bin(right)):
            if l != r:                
                break
        
        return calc(int(bin(left)[i:], 2), int(bin(right)[i:], 2))

    else:
        return (1 << (upper - 1)) ^ (1 << (upper - 2))


left, right = map(int, input().split())
print(calc(left, right))