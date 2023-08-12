class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        
        current_index = 0
                
        max_reachable = nums[current_index]
        
        for reachable_index in range(length):
            if reachable_index > max_reachable:
                current_index = max_reachable                                
                continue
            
            jump_range = reachable_index + nums[reachable_index]
                                        
            max_reachable = max(jump_range, max_reachable)
        
        
        return max_reachable >= length - 1