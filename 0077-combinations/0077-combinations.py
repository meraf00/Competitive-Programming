class Solution:  
    def __init__(self):
        self.solutions = []
        self.k = None        
    
    def backtrack(self, path, start, level, n):
        if level == 0:
            self.solutions.append(path)
            return
        
        for num in range(start, n + 1):            
            self.backtrack(path + [num], num + 1, level - 1, n)
        
    
  
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k = k
        
        self.backtrack([], 1, k, n)
                
        return self.solutions