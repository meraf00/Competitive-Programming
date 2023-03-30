class Solution:
    def countBits(self, n: int) -> List[int]:
        mask = 1
        
        ans = [0]
        
        most_significant_bit = 1
        
        for i in range(1, n + 1):
            if most_significant_bit & i == 0:
                most_significant_bit <<= 1
            
            inner = i & (~most_significant_bit)
            
            ans.append(ans[inner] + 1)
        
        return ans