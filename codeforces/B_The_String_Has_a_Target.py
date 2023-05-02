# https://codeforces.com/contest/1805/problem/B

test_cases = int(input())


for _ in range(test_cases):
    length = int(input())

    word = input()

    min_index = 0
    for i in range(1, length):
        if word[i] <= word[min_index]:
            min_index = i

    if min_index == 0:
        print(word)

    else:
        print(word[min_index] + word[:min_index] + word[min_index + 1 :])
