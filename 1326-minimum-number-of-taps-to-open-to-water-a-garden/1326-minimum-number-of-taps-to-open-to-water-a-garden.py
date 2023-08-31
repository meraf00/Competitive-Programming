class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        
        for tap_idx, tap_range in enumerate(ranges):
            intervals.append((max(0, tap_idx - tap_range), tap_idx + tap_range))
        
        intervals.sort()
        
        chain = [(0, 0)]                
        
        for interval in intervals:
            a, b = interval
            
            prev_a, prev_b = chain[-1]
            
            if b <= prev_b:
                continue
            
            if a > prev_b:
                return -1                    
            
            last_poped = None
            while len(chain) > 1 and chain[-1][1] > a:
                last_poped = chain.pop()
                
            
            if chain[-1][1] < a:
                chain.append(last_poped)                        
                        
            
            chain.append(interval)
            
            if b >= n:
                return len(chain) - 1
        
        return len(chain) - 1
            
            
            
"""
5
[0,1,0,1,0,1]
5
[3,4,1,1,0,0]
3
[0,0,0,0]
5
[1,1,1,1,1,1]
7
[1,2,1,0,2,1,0,1]
"""               
                
        
        
            
            
            
        
        
            