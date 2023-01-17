class Solution:
    def reverse_num(self, num):
        reversed_num = 0
        
        while num > 0:            
            reversed_num *= 10
            reversed_num += num % 10
            num //= 10
        
        return reversed_num
            
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distnict_nums = set(nums)
        
        for num in nums:
            reversed_num = self.reverse_num(num)
            
            distnict_nums.add(reversed_num)
        
        return len(distnict_nums)
        
        
        