class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        cycle_start = nums[0]
        while cycle_start != slow:
            cycle_start = nums[cycle_start]
            slow = nums[slow]        
            
        return cycle_start
        
        