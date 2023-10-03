class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        
        isPalindrom = [[False] * length for _ in range(length)]
        
        for i in range(length):
            isPalindrom[i][i] = True                    
        
        for gap in range(2, length + 1):
            for start in range(length - gap + 1):
                end = start + gap - 1
                if gap == 2 and s[start] == s[end]:
                    isPalindrom[start][end] = True
                    
                
                elif isPalindrom[start + 1][end - 1] and s[start] == s[end]:
                    isPalindrom[start][end] = True
        
        
        ans = []
        
        current = []
        
        def backtrack(start):
            if start >= length:
                ans.append(current[:])
                return
            
            for end in range(start, length):
                if isPalindrom[start][end]:
                    current.append(s[start:end+1])
                    backtrack(end + 1)
                    current.pop()                            
        
        backtrack(0)
        
        return ans
        
                    
                