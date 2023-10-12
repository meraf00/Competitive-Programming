class Solution:
    def compute_compatibility(self, student, mentor):
        total = 0

        for i, j in zip(student, mentor):
            if i == j:
                total += 1

        return total
        
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        
        comp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                comp[i][j] = self.compute_compatibility(students[i], mentors[j])
        
        @cache
        def backtrack(i, paired, score):            
            if i >= n:
                return score
            
            max_score = 0
            
            for j in range(n):
                if paired & (1 << j):
                    continue                                      
                
                s = backtrack(i + 1, paired ^ (1 << j), score + comp[i][j])
                
                max_score = max(s, max_score)
            
            return max_score
                
            
        return backtrack(0, 0, 0)
                