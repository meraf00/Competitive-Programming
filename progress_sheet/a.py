x = 123456

i = 3

copy_x = x
ith = 0
for _ in range(i):
    ith = copy_x % 10
    copy_x //= 10    

print(copy_x, ith)

prefix = ith * 10 ** (i - 1)
print(prefix)


print(x - copy_x * 10 ** (i))
