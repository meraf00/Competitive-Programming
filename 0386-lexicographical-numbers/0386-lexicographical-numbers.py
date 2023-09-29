class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
                               
        stack = [i for i in range(min(9, n), 0, -1)]
        
        ans = []
        
        while stack:
            current = stack.pop()
            
            ans.append(current)
            
            for i in range(9, -1, -1):                
                if current * 10 + i <= n:                     
                    stack.append(current * 10 + i)
        
        return ans
                    