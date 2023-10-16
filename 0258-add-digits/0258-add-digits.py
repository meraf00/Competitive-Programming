class Solution:
    def addDigits(self, num: int) -> int:
        if 0 <= num <= 9:
            return num
        
        s = 0
        
        while num:
            s += num % 10
            num //= 10
        
        return self.addDigits(s)