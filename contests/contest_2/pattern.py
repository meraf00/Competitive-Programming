patterns_count = int(input())

match = None

for i in range(patterns_count):
    pattern = input()
    pattern_length = len(pattern)
    if not match:
        match = [None] * pattern_length
    
    for i, char in enumerate(pattern):
        if char == "?":
            continue
        elif match[i] != None and match[i] != char:
            match[i] = "?"
        else:
            match[i] = char

for i in range(len(match)):
    if match[i] == None:
        match[i] = "x"
print("".join(match))
