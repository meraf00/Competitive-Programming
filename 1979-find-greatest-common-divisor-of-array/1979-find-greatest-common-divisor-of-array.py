class Solution:
    def euclid(self, a, b):        
        while b:
            temp = b
            a, b = temp, a % b
        
        return a
    
    def findGCD(self, nums: List[int]) -> int:
        return self.euclid(max(nums), min(nums))
            