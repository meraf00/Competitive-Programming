# https://codeforces.com/problemset/problem/1811/A

def insert_digit(num, d):
    new_num = []

    inserted = False

    for digit in num:
        if inserted or digit >= d:
            new_num.append(digit)

        else:
            new_num.append(d)
            new_num .append(digit)
            inserted = True

    if not inserted:
        new_num.append(d)

    return "".join(new_num)


test_cases = int(input())

for _ in range(test_cases):
    n_digits, digit_to_insert = input().split()

    num = input()

    print(insert_digit(num, digit_to_insert))
