class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        
        prefix = [[0] * (n + 1) for _ in range(26)]
        
        for i, char in enumerate(s):                        
            for j in range(26):
                idx = ord(char) - ord('a')
                
                if j == idx:
                    prefix[j][i + 1] = prefix[j][i] + 1
                
                else:
                    prefix[j][i + 1] = prefix[j][i]
        
        
        count = 0
        for i in range(n):
            for j in range(i, n):                
                max_freq = 0
                min_freq = float('inf')
                
                for k in range(26):                                    
                    if prefix[k][j + 1] - prefix[k][i] != 0:
                        max_freq = max(max_freq, prefix[k][j + 1] - prefix[k][i])
                        min_freq = min(min_freq, prefix[k][j + 1] - prefix[k][i])
            
                count += max_freq - min_freq                
        
        return count