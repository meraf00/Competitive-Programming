class Solution:    
    def strStr(self, haystack: str, needle: str) -> int:        
        MOD = 10 ** 9 + 7
        
        len_n = len(needle)
        len_h = len(haystack)
        
        if len_n > len_h:
            return -1
        
        base = 27
        
        power = {0: 1}
        
        for i in range(1, len_n + 1):
            power[i] = power[i - 1] * base
        
        
        def poll_first(h, char):
            asci = ord(char) - ord('a') + 1              
            return (h - asci * power[len_n - 1]) % MOD
        
        def add_last(h, char):
            return (h * base + (ord(char) - ord('a') + 1)) % MOD
        
        def compute_hash(string):
            n = len(string)
            hash = 0
            
            for i, char in enumerate(string):
                asci = ord(char) - ord('a') + 1
                
                hash += asci * power[n - i - 1]
                
            return hash % MOD                
        
        def compare_substring(left, right):
            for i in range(left, right + 1):                
                if haystack[i] != needle[i - left]:
                    return False
            
            return True
                                        
        target = compute_hash(needle)                 
        
        window_hash = compute_hash(haystack[:len_n])
        
        if target == window_hash:
            return 0
                                
        left = 0      
                                
        for right in range(len_n, len_h):
            window_hash = poll_first(window_hash, haystack[left]) 
                                        
            left += 1                                                  
                        
            window_hash = add_last(window_hash, haystack[right]) 
            
            
            if window_hash == target:
                if compare_substring(left, right):
                    return left
                                                                 
        return -1 
        