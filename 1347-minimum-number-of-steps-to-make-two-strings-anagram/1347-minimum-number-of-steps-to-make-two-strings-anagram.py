class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        
        steps = 0
        
        for char in t_count.keys():
            diff = s_count[char] - t_count[char]
            
            if diff < 0:
                steps += abs(diff)
            
        return steps