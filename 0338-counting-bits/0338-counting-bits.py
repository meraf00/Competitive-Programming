class Solution:
    def countBits(self, n: int) -> List[int]:
        mask = 1
        
        ans = []                
        
        for i in range(n + 1):
            count = 0
            
            while i:                        
                if i & mask == 1:
                    count += 1                        

                i >>= 1 
                
            ans.append(count)
        
        return ans