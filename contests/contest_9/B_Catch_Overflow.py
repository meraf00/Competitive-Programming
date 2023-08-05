lines = int(input())


stack = [1]
x = 0
limit = 2**32 - 1

for _ in range(lines):
    cmd = input()
    
    if x > limit: continue

    if cmd[0] == "f":
        n = int(cmd.split()[1])                
        stack.append(stack[-1] * n)
    
    elif cmd[0] == "a":
        x += stack[-1]
    
    elif cmd[0] == "e":
        stack.pop()

if x > limit:
    print("OVERFLOW!!!")
else:
    print(x)

