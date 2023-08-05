def color(n):
    PRIME = "1"
    COMPOSITE = "2"

    n = n + 2

    nums = [PRIME] * n
    nums[0] = nums[1] = COMPOSITE

    for i in range(4, n, 2):
        nums[i] = COMPOSITE

    for i in range(3, n, 2):
        if nums[i] == PRIME:
            for j in range(i * i, n, i):
                nums[j] = COMPOSITE

    return " ".join(nums[2:])


n = int(input())

colors = color(n)

if "1" in colors and "2" in colors:
    print(2)
else:
    print(1)

print(colors)
