"""https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true"""

# Enter your code here. Read input from STDIN. Print output to STDOUT


def is_pilling_possible(blocks):
    left = 0
    right = len(blocks) - 1

    prev = float('inf')
    while left <= right:
        if blocks[right] >= blocks[left] and blocks[right] <= prev:
            prev = blocks[right]
            right -= 1
        elif blocks[left] <= prev:
            prev = blocks[left]
            left += 1
        else:
            return False

    return True


# Taking test cases
n_tests = int(input())

for i in range(n_tests):
    number_of_cubes = int(input())
    blocks = list(map(int, input().split(" ")))

    if is_pilling_possible(blocks):
        print("Yes")
    else:
        print("No")
