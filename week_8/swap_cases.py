"""https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true"""


def swap_case(s):
    s = list(s)
    for i, char in enumerate(s):
        ascii = ord(char)
        if 65 <= ascii <= 90:
            ascii += 32
        elif 97 <= ascii <= 122:
            ascii -= 32
        s[i] = chr(ascii)

    return "".join(s)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
