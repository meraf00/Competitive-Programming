class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n_houses = len(colors)                
        
        max_distance = 0
        
        for i in range(n_houses):                 
            if colors[i] != colors[0]:                
                max_distance = max(max_distance, i)
            
            if colors[i] != colors[-1]:
                max_distance = max(max_distance, n_houses - i - 1)
        
        return max_distance
                