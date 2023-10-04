class Solution:
    def minimumCost(self, s: str) -> int:
        length = len(s)
        
        prefix = [0] * length
        
        suffix = [0] * length
        
        for i in range(1, length):
            if s[i] == s[i - 1]:
                prefix[i] = prefix[i - 1]                
            
            else:
                prefix[i] = prefix[i - 1] + i
            
            j = length - i - 1
            
            if s[j] == s[j + 1]:
                suffix[j] = suffix[j + 1]
            
            else:
                suffix[j] = suffix[j + 1] + (length - j - 1)
        
        min_cost = float('inf')
        
        for pre, suff in zip(prefix, suffix):
            min_cost = min(pre + suff, min_cost)
            
        return min_cost
            
        