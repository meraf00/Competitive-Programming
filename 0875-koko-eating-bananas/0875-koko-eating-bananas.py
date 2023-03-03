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
        high = sum(piles)
        low = high // h
                
        while low <= high:
            mid = low + (high - low) // 2
            # print(high, low, mid)
            
            if self.time_required(mid, piles) <= h:                
                high = mid - 1
                
            else:
                low = mid + 1                     
            
            # print(locals())
            # print()
                        
        # if self.time_required(high - 1, piles) <= h:
        #     return high - 1
        
        return low