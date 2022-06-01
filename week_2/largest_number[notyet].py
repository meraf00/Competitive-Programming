from typing import List

class Solution:
    def get_digits(self, num: int) -> str:
        if num == 0:
            return 1
        
        digits = 0
        while num:
            num //= 10            
            digits += 1
        return digits
    
    def largestNumber(self, nums: List[int]) -> str:
        max_digit = max(map(self.get_digits, nums))
        
        d = {}
        
        for n in nums:
            digits = self.get_digits(n)
            if digits in d.keys():
                d[digits].append(n)
            else:
                d[digits] = [n]
        
        for value in d.values():
            value.sort()
        print(d)
                
        
if __name__ == "__main__":
    soln = Solution()
    soln.largestNumber([10, 2])
    soln.largestNumber([3,30,34,5,9])
    
