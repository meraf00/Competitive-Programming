class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int: 
        max_num1 = max(nums1)
        min_num1 = min(nums1)
        
        max_num2 = max(nums2)                
        min_num2 = min(nums2)
        
        if max_num1 < 0 and min_num2 > 0:
            return max_num1 * min_num2
    
        if max_num2 < 0 and min_num1 > 0:
            return max_num2 * min_num1
        
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]        
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = max(
                    dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1],                    
                    dp[i - 1][j],
                    dp[i][j - 1]
                )                   
            
        return dp[-1][-1]
                
                    
                    
        
"""
[-3,-8,3,-10,1,3,9]
[9,2,3,7,-9,1,-8,5,-1,-1]
"""        
        