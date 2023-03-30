class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        
        for i in range(length):
            current = nums[i]
            
            while current - 1 != i:
                if nums[current - 1] == current:
                    break
                    
                nums[i], nums[current - 1] = nums[current - 1], nums[i]
                
                current = nums[i]
        
        for i in range(length):
            if nums[i] - 1 !=  i:
                return nums[i]
                
                
            