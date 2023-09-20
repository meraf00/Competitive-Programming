class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        rng = [0] * (hi - lo + 1)
        
        @lru_cache(None)
        def dp(n):
            if n == 1:
                if lo <= n <= hi:
                    rng[n - lo] = 0
                return 0
            
            # even
            if n & 1 == 0:                
                val = dp(n // 2) + 1
                
            
            else:
                val = dp(3 * n + 1) + 1
            
            if lo <= n <= hi:
                rng[n - lo] = val
            
            return val
        
        for i in range(lo, hi + 1):
            dp(i)                                        
        
        ans = []
        for i, n in enumerate(rng):
            ans.append((n, i))
        
        ans.sort()                
        
        return ans[k - 1][1] + lo
            
            
        
        
        
            
            