"""https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true"""

if __name__ == '__main__':
    N = int(input())

    internal_list = []

    for _ in range(N):
        line = input().split()
        command = line[0]

        if command == "print":
            print(internal_list)

        else:
            function = getattr(internal_list, command)
            if len(line) > 1:
                args = map(int, line[1:])
                function(*args)
            else:
                function()
