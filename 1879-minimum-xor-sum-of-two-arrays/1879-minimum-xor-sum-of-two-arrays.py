class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        length = len(nums1)
        
        @cache
        def dp(bitmask, k):
            if k >= length:                
                if bitmask + 1 == (1 << (length)):
                    return 0
                return float('inf')
            
            result = float('inf')
            
            for i, n in enumerate(nums2):
                if bitmask & (1 << i):
                    continue
                
                result = min(
                    dp(bitmask ^ (1 << i), k + 1) + (n ^ nums1[k]), 
                    # dp(bitmask, k + 1),
                    result)
                
            
            return result
                
                
        return dp(0, 0)    
        
                