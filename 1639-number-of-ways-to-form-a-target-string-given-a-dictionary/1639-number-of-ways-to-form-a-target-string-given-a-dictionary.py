class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        
        counter = [[0] * n for _ in range(26)]
        
        for word in words:
            for col, char in enumerate(word):
                row = ord(char) - ord('a')                
                counter[row][col] += 1
        

        @cache
        def dp(i, k):                        
            if i >= len(target):                
                return 1
            
            if k >= n:
                return 0
                                                    
            count = 0
            
            char = target[i]
            row = ord(char) - ord('a')
                        
            # take current idx             
            next_count = dp(i + 1, k + 1)
            curr_count = counter[row][k]                        
            count += ((next_count % mod) * (curr_count % mod)) % mod            
            count %= mod
            
            
            # not take
            next_count = dp(i, k + 1)                                   
            count += next_count % mod            
            count %= mod
            
            return count
        
        mod = pow(10, 9) + 7
        return dp(0, 0) % mod
                        