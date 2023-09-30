class Solution:
    def largestInteger(self, num: int) -> int:
        odd_digits = []
        even_digits = []
        odd = []
        
        while num:            
            digit = num % 10
            
            if digit & 1:
                odd.append(True)
                odd_digits.append(-digit)
            else:
                odd.append(False)
                even_digits.append(-digit)
                        
            num //= 10
        
        
        heapify(odd_digits)
        heapify(even_digits)
        
        ans = 0
        for is_odd in reversed(odd):
            if is_odd:
                digit = -heappop(odd_digits)            
            else:
                digit = -heappop(even_digits)
                
            ans *= 10
            ans += digit
        
        return ans
        
        
        