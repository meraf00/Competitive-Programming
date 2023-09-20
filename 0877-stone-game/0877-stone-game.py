class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n_piles = len(piles)
        
        ALICE = 0     
        BOB = 1
                
        @lru_cache(None)
        def dp(i, j, player):
            if i > j:
                return 0
            
            # alice 
            if player == ALICE:
                return max(piles[i] + dp(i + 1, j, BOB), piles[j] + dp(i, j - 1, BOB))
        
            else:
                return min(-piles[i] + dp(i + 1, j, ALICE), piles[j] + dp(i, j - 1, BOB))
        
        return dp(0, n_piles - 1, ALICE) > 0