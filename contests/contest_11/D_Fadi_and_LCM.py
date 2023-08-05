def factorize(n):
    # returns prime factors of n but multiplies prime factors if they appear morethan once
    # eg for n = 30 [2,3,5] -> [2,3,5]
    # eg for n = 60 [2, 2,3,5] -> [4,3,5]

    factorization = []

    i = 2
    for i in range(2, n):
        while n % i == 0:
            if factorization and factorization[-1] == i:
                factorization[-1] *= i
            else:
                factorization.append(i)
            n //= i

    if n % i == 0:
        factorization.append(i)

    return factorization


def minimize_2_factors(factorization, num):
    n_factors = len(factorization)
    
    num1 = []
    num2 = []

    num_1, num_2 = 1, num
    
    def backtrack(idx):
        nonlocal num_1, num_2

        if len(num1) + len(num2) == n_factors:
            n1 = 1
            n2 = 1
            for n in num1:
                n1 *= n
            
            for n in num2:
                n2 *= n

            if max(n1, n2) < max(num_1, num_2):
                num_1 = n1
                num_2 = n2
            return        
        
        # print(num1, num2)
        for i in range(idx, n_factors):
            num1.append(factorization[i])
            backtrack(i + 1)            
            num1.pop()

            num2.append(factorization[i])
            backtrack(i + 1)
            num2.pop()
        
        return
    

    backtrack(0)        
        
    return min(num_1, num_2), max(num_1, num_2)
    



n = int(input())

prime_factorization = factorize(n)

print(*minimize_2_factors(prime_factorization, n))
