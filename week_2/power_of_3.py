class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        
        if n and n % 3 == 0:        
            return self.isPowerOfThree(n // 3)
        
        return False            