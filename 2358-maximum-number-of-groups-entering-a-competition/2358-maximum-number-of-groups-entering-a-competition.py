class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        
        k = (sqrt(8 * n + 1) - 1) / 2
        
        return int(k)
        
        