class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        
        x = abs(x)
        reversed_ = 0
        while x:
            reversed_ = reversed_ * 10 + (x % 10)
            x //= 10
        
        output = sign * reversed_
        
        if -2**31 <= output <= 2**31 - 1:
            return output
        return 0