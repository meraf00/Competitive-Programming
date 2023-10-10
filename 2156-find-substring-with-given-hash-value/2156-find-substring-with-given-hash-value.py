class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        if k > len(s):
            return -1
        
        powers = {0: 1}
        
        for i in range(1, k):
            powers[i] = powers[i - 1] * power                    
        
        def poll_first(h, char):
            asci = ord(char) - ord('a') + 1            
            return (h - asci * powers[k - 1]) % modulo
                    
        def add_last(h, char):
            asci = ord(char) - ord('a') + 1
            return (h * power + asci) % modulo
                    
        def hash_(string):
            h = 0
            n = len(string)
            
            for i in range(len(string)):
                asci = ord(string[i]) - ord('a') + 1
                
                h += asci * powers[n - i - 1]
            
            return h % modulo
        
        
        s = ''.join(reversed(s))
        
        
        window_hash = hash_(s[:k])
        
        ans = None
        
        if window_hash == hashValue:
            ans = s[:k]
              
        for right in range(k, len(s)):            
            window_hash = poll_first(window_hash, s[right - k])
            
            window_hash = add_last(window_hash, s[right])                         
            
            if window_hash == hashValue:
                ans = s[right - k + 1:right + 1]            
                        
                
        return ans[::-1]