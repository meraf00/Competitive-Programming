class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        
        degree.sort()
        
        total_importance = 0
        
        for idx, repeated in enumerate(degree):
            total_importance += (idx + 1) * repeated
        
        return total_importance