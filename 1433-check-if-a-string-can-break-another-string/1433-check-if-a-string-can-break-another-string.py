class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        
        s1.sort()
        s2.sort()
               
        s1_breaks_s2 = True
        s2_breaks_s1 = True
        
        for a, b in zip(s1, s2):
            s1_breaks_s2 = s1_breaks_s2 and b <= a 
            s2_breaks_s1 = s2_breaks_s1 and a <= b
        
        return s1_breaks_s2 or s2_breaks_s1
                
        
        
            