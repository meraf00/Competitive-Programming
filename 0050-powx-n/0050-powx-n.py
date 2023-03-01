class Solution:
    def myPow(self, x: float, n: int) -> float:    
        if n == 1:
            return x
        if n == 0:
            return 1
        
        if n > 0:
            half_powered = self.myPow(x, n // 2)
            
            if n % 2 == 0:                
                return half_powered * half_powered
            else:
                return half_powered * half_powered * x
        
        elif n < 0:
            return self.myPow(1 / x, -n)
        
        
            
                
        