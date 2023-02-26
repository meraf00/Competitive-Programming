class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        
        total_product = 1
        
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
        
        if zero_count == 0:
            for i, num in enumerate(nums):
                nums[i] = total_product // num  
        
        elif zero_count == 1:
            for i, num in enumerate(nums):
                if num != 0:
                    nums[i] = 0
                    continue                
                nums[i] = total_product                
        else:
            for i in range(len(nums)):
                nums[i] = 0
        
        return nums