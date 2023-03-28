class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [-1]
        
        arr.append(float("-inf"))
        
        count = 0
        
        for current_index, num in enumerate(arr):
            
            while stack and arr[stack[-1]] > num:                
                index = stack.pop()
                count += arr[index] * (current_index - index) * (index - stack[-1])
                
            stack.append(current_index)
            
            
        return count % (10**9 + 7)
        