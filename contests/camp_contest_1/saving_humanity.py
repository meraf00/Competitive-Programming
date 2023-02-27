test_cases = int(input())


def revive(humans):
    new = [humans[0]]

    if humans[0] == "0" and humans[1] == "1":
        new[0] = "1"

    humans.append("0")
    for i in range(1, len(humans) - 1):

        if humans[i] != "0":
            new.append(humans[i])
            continue

        prev = humans[i-1]
        next = humans[i+1]

        if prev != next and (prev == "1" or next == "1"):
            new.append("1")
        else:
            new.append("0")

    return new


def process(humans, iter):
    if len(humans) <= 1:
        return "".join(humans)

    for _ in range(iter):
        humans = revive(humans)

    return "".join(humans)


for _ in range(test_cases):
    size, iter = list(map(int, input().split()))

    humans = list(input())

    print(process(humans, iter))
