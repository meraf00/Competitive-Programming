class Solution:
    def countBits(self, n: int) -> List[int]:
        mask = 1
        
        ans = [0, 1]
        
        for i in range(2, n + 1):                        
            ans.append(ans[i & (i - 1)] + 1)
        
        return ans[:n+1]