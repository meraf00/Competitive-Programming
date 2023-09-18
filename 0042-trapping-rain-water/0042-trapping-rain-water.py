class Solution:                
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        prefix_max = [0] * n
        suffix_max = [0] * n
        
        for i in range(n):
            left = height[i]
            right = height[~i]
            
            prefix_max[i] = max(left, prefix_max[i - 1])
            suffix_max[~i] = max(right, suffix_max[~(i - 1)])
            
        
        total = 0
        
        for h, pmax, smax in zip(height, prefix_max, suffix_max):
            total += min(pmax, smax) - h 
            
        return total
        