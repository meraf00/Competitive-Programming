class Solution:
    def rob(self, nums: List[int]) -> int:                
        houses = len(nums)
        
        computed = {}
        
        def dp(house_idx):
            if house_idx in computed:
                return computed[house_idx]
            
            if house_idx < 0:
                return 0
            
            computed[house_idx] = max(dp(house_idx - 2), dp(house_idx - 3)) + nums[house_idx]
            
            return computed[house_idx]
            
                
        return max(dp(houses - 1), dp(houses - 2))