class Solution:    
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [1] * (right + 1)
        is_prime[0] = is_prime[1] = 0
        
        for i in range(4, right + 1, 2):
            is_prime[i] = 0
        
        for i in range(3, int(sqrt(right)) + 1, 2):
            if is_prime[i]:
                j = i * i
                while j <= right:
                    is_prime[j] = 0
                    j += i
                        
        
        r = right
        while not is_prime[r] and r > left:
            r -= 1
        
        if left == r:
            return [-1, -1]
        
        num1 = float("-inf")
        num2 = float("inf")
        for l in range(r - 1, left - 1, -1):              
            if is_prime[l]:
                if num2 - num1 >= r - l:
                    num1 = l
                    num2 = r
                r = l
        
        if num2 == float("inf"):
            return [-1, -1]
        
        return [num1, num2]
                
            
            
            
            
        