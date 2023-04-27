class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length  = len(nums)
        
        maximum = max(nums)
        
        for i in range(length):
            # handle negatives
            if nums[i] <= 0:
                nums[i] = 0
            
            # handle out of bound numbers
            if nums[i] >= length:
                nums[i] = maximum
        
        for i in range(length):
            current = nums[i]
                        
            while current - 1 != i:
                if current >= length:
                    break
                    
                # duplicate
                if nums[current - 1] == current:                    
                    break
                    
                nums[i], nums[current - 1] = nums[current - 1], nums[i]
                current = nums[i]
        
        
        for i, num in enumerate(nums):
            if num - 1 != i:
                return i + 1                
        
        return maximum + 1
        
        
    