"""https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

if __name__ == "__main__":
    first_line = input().split()
    group_a_size = int(first_line[0])
    group_b_size = int(first_line[1])

    char_index = defaultdict(list)
    for index in range(group_a_size):
        char = input()
        printable_index = str(index + 1)
        char_index[char].append(printable_index)

    for index in range(group_b_size):
        char = input()
        if char in char_index:
            output = " ".join(char_index[char])
        else:
            output = -1
        print(output)
