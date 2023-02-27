n_ingredients = int(input())

ingredients = list(map(int, input().split()))

prefix_sum = [ingredients[0]] * n_ingredients

for i in range(1, n_ingredients):
    prefix_sum[i] = prefix_sum[i - 1] + ingredients[i]

total = prefix_sum[-1]
suffix_sum = [total]
for i in range(1, n_ingredients):
    suffix_sum.append(total - prefix_sum[i-1])

E = 0
A = 0
for i in range(n_ingredients):
    if prefix_sum[i] <= suffix_sum[i]:        
        E += 1
    else:
        A += 1
        
print(E, A)