string = input()


ab = set()
ba = set()
count = 0


for i in range(len(string) - 1):
    s = string[i:i+2]
    if s == "AB":
        if i not in ba and i + 1 not in ba and len(ba) != 0:
            print("YES")
            quit()
            
        ab.update([i, i + 1])
        
    
    if s == "BA":
        if i not in ab and i + 1 not in ab and len(ab) != 0:
            print("YES")
            quit()

        ba.update([i, i+1])

if len(ab) > 2 and len(ba) > 2:
    print("YES")

else:
    print("NO")
