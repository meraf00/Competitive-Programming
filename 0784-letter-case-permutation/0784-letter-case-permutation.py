class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        
        res = set()
        
        current = []
        
        def backtrack(i):
            if i >= n:
                res.add(''.join(current))
                return
            
            if s[i].isalpha():
                current.append(s[i].lower())
                backtrack(i + 1)
                current.pop()
                
                current.append(s[i].upper())
                backtrack(i + 1)
                current.pop()
            
            else:
                current.append(s[i])
                backtrack(i + 1)
                current.pop()
         
        backtrack(0)
        return res    
                
            