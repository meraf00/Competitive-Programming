class Solution:
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        elif len(nums) == 2:
            return [nums, list(reversed(nums))]
        
        all_perms = []
        for index, num in enumerate(nums):
            nums_without_current_num = nums[:index]
            if index + 1 <= len(nums):
                nums_without_current_num.extend(nums[index + 1:])
            
            permutuation_without_current_num = self.permute(nums_without_current_num)            
            for perm in permutuation_without_current_num:
                all_perms.append([num] + perm)                
        
        return all_perms