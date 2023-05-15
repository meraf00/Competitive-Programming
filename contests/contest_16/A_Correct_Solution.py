num = list(input())
ans = input()
num.sort()

i = 0
for i in range(len(num)):
    if num[i] != "0":        
        break

if i == 0:
    n = "".join(num)

else:
    n = "".join([num[i]] + num[:i] + num[i+1:])


if n == ans:
    print("OK")

else:
    print("WRONG_ANSWER")
