# src: Admas

cases = int(input())

for i in range(cases):
    phrases = input().split()

    order = []
    rank = -1

    for i, phrase in enumerate(phrases):
        for j, char in enumerate(phrase):
            if char.isnumeric():
                rank += 1
                order.append([int(char), i])

    order.sort(key=lambda x: x[0])
    for k, p in enumerate(phrases):
        s = ""
        for z, ch in enumerate(p):
            if ch.isnumeric():
                continue
            else:
                s += ch
        phrases[k] = s

    res = ""
    for a, b in order:
        res += (phrases[b] + " ")
    print(res[:len(res)-1])
