class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = set()
        
        for i in range(len(nums)):
            current = nums[i]
            
            if current in duplicates:
                continue
            
            while current - 1 != i:
                if nums[i] == nums[current - 1]:
                    duplicates.add(current)
                    
                nums[i], nums[current - 1] = nums[current - 1], nums[i]
                
                current = nums[i]
                
                if current in duplicates:                    
                    break
        
        return list(duplicates)
        