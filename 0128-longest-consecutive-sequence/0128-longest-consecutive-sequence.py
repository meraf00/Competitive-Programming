class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:           
        cons = {}
        visited = set()
        max_range = 0
        
        for num in nums:    
            if num in visited:
                continue
            visited.add(num)
            
            low = num
            high = num
            
            if num + 1 in cons:
                high = cons[num + 1][1]
            
            if num - 1 in cons:
                low = cons[num - 1][0]
            
            cons[low] = [low, high]
            cons[high] = [low, high]
                        
                
            max_range = max(high - low + 1, max_range)
            
            
        return max_range                