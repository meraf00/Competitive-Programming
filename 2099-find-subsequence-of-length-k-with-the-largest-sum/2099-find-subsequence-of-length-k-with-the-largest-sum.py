class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
                
        ans = []
        
        for i, num in enumerate(nums):
            heappush(ans, (num, i))
            
            if len(ans) > k:
                heappop(ans)
        
        ans.sort(key = lambda x: x[1])
        return list(map(lambda x:x[0], ans))
            