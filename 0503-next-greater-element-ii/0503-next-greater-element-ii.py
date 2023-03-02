class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        
        size = len(nums)
        
        output = [-1] * size
        
        for right in range(size * 2):
            right = right % size
            
            while stack and nums[stack[-1]] < nums[right]:
                index = stack.pop()
                output[index] = nums[right]

            stack.append(right)            
        
        return output