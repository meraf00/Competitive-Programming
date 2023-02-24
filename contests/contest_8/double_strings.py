# https://codeforces.com/gym/428168/problem/C

def double_stings(strings):
    strings_set = set(strings) 

    ans = ["0"] * len(strings)
    for string_index, string in enumerate(strings):
        for i in range(1, len(string)):
            prefix = string[:i]
            suffix = string[i:]

            if prefix in strings_set and suffix in strings_set:
                ans[string_index] = '1'
    return "".join(ans)


test_cases = int(input())

for _ in range(test_cases):
    num_strings = int(input())

    strings = []
    for i in range(num_strings):
        strings.append(input())
    
    print(double_stings(strings))