class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        else:
            sign = 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if dividend < divisor:
            return 0
        
        if dividend == divisor:
            return 1 * sign
        
        d = divisor
        
        shift = 1
        while d < dividend:
            d <<= 1
            shift <<= 1
        
        if d == dividend:
            quotient = sign * shift
        
        else:
            d >>= 1

            remainder = dividend - d                                

            quotient = sign * ((shift >> 1) + self.divide(remainder, divisor))
        
        if quotient > (2 ** 31) - 1:
            return (2 ** 31) - 1
    
        elif quotient < -(2 ** 31):
            return -(2 ** 31)
        
        else:
            return quotient
            