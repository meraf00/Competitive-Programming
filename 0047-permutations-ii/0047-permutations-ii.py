class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        elif len(nums) == 2:
            if nums[0] != nums[1]:            
                return [nums, list(reversed(nums))]            
            return [nums]
        
        all_perms = []
        for index, num in enumerate(nums):
            nums_without_current_num = nums[:index]
            if index + 1 <= len(nums):
                nums_without_current_num.extend(nums[index + 1:])
            
            permutuation_without_current_num = self.permuteUnique(nums_without_current_num) 
            
            for perm in permutuation_without_current_num:
                all_perms.append([num] + perm)                
        
        unique_perms_set = set()
        for perm in all_perms:
            unique_perms_set.add(tuple(perm))                    
        
        unique_perms = []
        for perm in unique_perms_set:
            unique_perms.append(list(perm))
            
        return unique_perms