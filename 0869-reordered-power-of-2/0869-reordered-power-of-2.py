class Solution:
    def countDigit(self, n):
        counter = [0] * 10
        while n > 0:
            counter[n % 10] += 1
            n //= 10
        
        return tuple(counter)
    
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_2 = [1 << i for i in range(31)] 
        
        digit_count = self.countDigit(n)
        
        for num in power_of_2:            
            if self.countDigit(num) == digit_count:
                return True        
        
        return False