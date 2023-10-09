class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:        
        if len(set(a)) < len(set(b)):
            return -1                
        
        len_a = len(a)
        len_b = len(b)
        
        possible = set()
        
        for i in range(len_a):
            possible.add((a[i - 1], a[i]))
                    
        for i in range(1, len_b):
            if (b[i - 1], b[i]) not in possible:                
                return -1
            
            
        lps = [0] * len_b
        
        i, j = 0, 1
        
        while j < len_b:
            if b[i] == b[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            
            elif i == 0:
                j += 1
            
            else:
                i = lps[i - 1]
            
            
        i, j = 0, 0
        
        count = 1
        
        while j < len_a:            
            if a[j] == b[i]:                
                i += 1
                j += 1
                
            elif i == 0:
                j += 1
            
            else:
                i = lps[i - 1]
            
            if i == len_b:
                return count
            
            if j == len_a:
                j = j % len_a
                count += 1
            
            if count > len_b:
                return -1
            
                                
        return -1
            
        
"""
"abcd"
"cdabcdab"
"a"
"aa"
"abc"
"wxyz"
"aaac"
"aac"
 """       