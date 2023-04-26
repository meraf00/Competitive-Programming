def almost_prime(num): 
    x = num   
    d = 2

    factorization = set()
            
    while d * d <= num:        
        while num % d == 0:            
            factorization.add(d)
            num //= d

        d += 1

    if num > 1:
        factorization.add(num)
    
    return len(factorization) == 2


def almost_primes(num):
    count  = 0

    for num in range(2, num + 1):
        if almost_prime(num):            
            count += 1
    
    return count


print(almost_primes(int(input())))