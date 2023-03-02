class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        
        mid = float("-inf")
        
        for right in range(len(nums)):
            if nums[~right] < mid:
                return True
            
            while stack and nums[stack[-1]] < nums[~right]:            
                
                mid = nums[stack[-1]]
                
                stack.pop()
            
            stack.append(~right)
        
        return False