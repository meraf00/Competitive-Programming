class Solution: 
    def isValid(self, count):
        for val in count.values():
            if val > 0:
                return False
            
        return True
    
    def balancedString(self, s: str) -> int:        
        length = len(s)
        
        
        # required freq per char
        required = length // 4
        
                
        extras = Counter(s)
        
        # make extras count the extra characters we need to remove
        for char in "QWER":
            extras[char] = max(0, extras[char] - required)
        
        
        # already balanced
        if self.isValid(extras):
            return 0
        
        
        left = 0
                
        min_substring = length
        
        for right in range(length):
            
            extras[s[right]] -= 1
            
            while self.isValid(extras):
                
                min_substring = min(min_substring, right - left + 1)
                
                extras[s[left]] += 1
                
                left += 1
        
        return min_substring
            
            