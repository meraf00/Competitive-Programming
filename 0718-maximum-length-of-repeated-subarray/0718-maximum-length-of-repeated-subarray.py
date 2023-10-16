class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        ans = 0
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                ans = max(dp[i][j], ans)
        
        return ans