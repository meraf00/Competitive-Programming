class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
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
        
        missing = []
        for i, num in enumerate(nums):
            if num - 1 != i:
                missing.append(i + 1)
            
        
        return missing
                
                
            
        
        
        