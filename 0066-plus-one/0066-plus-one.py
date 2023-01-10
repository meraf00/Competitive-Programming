class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        next_num = []
        for digit in reversed(digits):
            next_num.append((digit + carry) % 10)
            if digit + carry > 9:
                carry = 1
            else:
                carry = 0
        
        if carry:
            next_num.append(carry)
        
        next_num = list(reversed(next_num))
        
        return next_num
            
            
                
        