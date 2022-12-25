"""https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true"""


def wrap(string, max_width):
    output = []

    string_length = len(string)
    for i in range(string_length // max_width + 1):
        start_index = max_width * i
        end_index = min(start_index + max_width, string_length)

        if end_index < string_length:
            output.append(string[start_index:end_index])
        else:
            output.append(string[start_index:])

    output = "\n".join(output)

    return output


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
