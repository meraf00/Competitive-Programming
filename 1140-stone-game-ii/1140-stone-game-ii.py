class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        length = len(piles)
        
        ALICE = True        
        
        prefix = [0]
        for pile in piles:
            prefix.append(prefix[-1] + pile)           
                
        
        @cache
        def dp(start, M, player): 
            if start >= length:                
                return 0
            
            max_score = float('-inf')
            min_score = float('inf')
            
            for X in range(1, min(2*M, length - start) + 1):
                end = start + X               
                                
                n_stone = prefix[end] - prefix[start]                
                
                if player == ALICE:                                         
                    new_score = dp(end, max(M, X), not player) + n_stone
                    max_score = max(new_score, max_score)
                    
                else:                    
                    new_score = dp(end, max(M, X), not player)
                    min_score = min(new_score, min_score)
                
                
            if player == ALICE:
                return max_score
            
            return min_score
                
            
        
        ans = dp(0, 1, ALICE)
        
        return ans