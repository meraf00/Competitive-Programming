class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        len_t = len(t)
        
        freq = Counter(t)
        
        chars = list(set(t))
        
        def isValid(counter):
            for char in chars:
                if counter[char] < freq[char]:
                    return False
            
            return True
            
        
        left = 0
        
        window_count = defaultdict(int)
        
        ans = ''
        min_window_substring = float('inf')
        
        for right in range(n):                            
            if s[right] in freq:
                window_count[s[right]] += 1
            
            while left <= right and s[left] not in freq:
                left += 1
            
            while isValid(window_count):                
                if right - left + 1 < min_window_substring:
                    min_window_substring = right - left + 1
                    ans = s[left:right + 1]
                
                if s[left] in freq:
                    window_count[s[left]] -= 1
                    
                left += 1
               
            if min_window_substring == len_t:
                break                                    
        
        return ans
                
            
            