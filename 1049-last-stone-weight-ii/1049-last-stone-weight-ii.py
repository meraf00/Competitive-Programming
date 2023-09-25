class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n_stones = len(stones)                
        
        total = sum(stones)
        
        @cache
        def dp(idx, current_sum):
            if idx >= n_stones:
                return current_sum        
            
            option1 = current_sum + stones[idx]
            sum_one = dp(idx + 1, option1)
                        
            option2 = current_sum - stones[idx]
            sum_two = dp(idx + 1, option2)
                        
            
            if sum_one < 0:
                return sum_two
            
            if sum_two < 0:
                return sum_one
            
            return min(sum_one, sum_two)
        
        
        return dp(0, 0)