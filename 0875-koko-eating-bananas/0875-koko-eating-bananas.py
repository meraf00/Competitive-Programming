class Solution:
    def time_required(self, rate, piles):  
        if rate == 0:
            return float('inf')
            
        total_time = 0
        
        for pile in piles:
            if pile % rate == 0:
                total_time += pile // rate
            else:
                total_time += pile // rate + 1    
        
        return total_time
        
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        high = max(piles)
        low = sum(piles) // h
                
        while low <= high:
            mid = low + (high - low) // 2            
            
            if self.time_required(mid, piles) <= h:                
                high = mid - 1
                
            else:
                low = mid + 1                     

        return low