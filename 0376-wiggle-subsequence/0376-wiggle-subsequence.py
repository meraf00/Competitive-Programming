class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        increasing = [0] * n
        decreasing = [0] * n
        
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    increasing[i] = max(increasing[i], decreasing[j] + 1)
                
                elif nums[i] < nums[j]:
                    decreasing[i] = max(decreasing[i], increasing[j] + 1)
                
                    
        return max(increasing[-1], decreasing[-1]) + 1
        