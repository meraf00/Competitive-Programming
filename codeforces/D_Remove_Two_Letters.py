test_cases = int(input())

for _ in range(test_cases):
    n = int(input())

    string  = input()

    seen = set([hash(string[2:])])
    for i in range(n - 1):        
        seen.add(hash(string[:i] + string[i+2:]))

    print(len(seen))