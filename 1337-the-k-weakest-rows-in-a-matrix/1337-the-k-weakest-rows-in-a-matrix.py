class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        
        for idx, row in enumerate(mat):            
            rows.append((sum(row), idx))
            
        rows.sort()
        
        answer = []
        
        for _, row in rows[:k]:
            answer.append(row)
            
                    
        return answer
                
            
            