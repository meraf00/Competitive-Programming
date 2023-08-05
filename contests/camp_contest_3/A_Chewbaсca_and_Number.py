num = input()


output = []
for digit in num[1:]:
    value = int(digit)
    if value >= 5:
        output.append(str(9 - value))

    else:
        output.append(digit)

if num[0] == "9" and int("".join(output)) == 0:
    print(int("9" + "".join(output)))

elif int(num[0]) >= 5:
    print(int(str(9 - int(num[0])) + "".join(output)))

else:
    print(int(num[0] + "".join(output)))

