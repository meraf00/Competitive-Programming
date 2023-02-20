class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left = 0
        right = len(skill) - 1
        
        target = skill[left] + skill[right]
        
        chemistry = 0
        
        while left < right:
            a, b = skill[left], skill[right]
            if a + b != target:
                return -1
            
            chemistry += a * b
            left += 1
            right -= 1
        
        return chemistry
            
            
        
        
        