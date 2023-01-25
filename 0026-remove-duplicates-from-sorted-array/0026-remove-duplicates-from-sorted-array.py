class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        non_duplicate = 0

        for i in range(len(nums)):            
            
            if nums[non_duplicate] != nums[i]:            
                non_duplicate += 1
            
            nums[non_duplicate] = nums[i] 
                        
        return non_duplicate + 1

        