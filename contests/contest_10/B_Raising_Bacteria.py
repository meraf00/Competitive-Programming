def min_bac(n):
    nearest_power_of_2 = 1 << (n.bit_length() - 1)

    if n - nearest_power_of_2 == 0:
        return 1

    return 1 + min_bac(n - nearest_power_of_2)

n = int(input())


print(min_bac(n))