class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:        
        length = len(nums)
        
        for i in range(length):            
            current = nums[i]                        
            
            while current - 1 != i:
                if current == nums[current - 1]:
                    break
                
                nums[current - 1], nums[i] = nums[i], nums[current - 1]
                
                current = nums[i]
                
        

        for i in range(length):
            if nums[i] - 1 != i:
                return [nums[i], i + 1]
