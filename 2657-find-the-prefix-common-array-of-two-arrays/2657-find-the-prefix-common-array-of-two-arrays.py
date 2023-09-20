class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_a = set()
        seen_b = set()
        
        c = []
        
        intersection_count = 0
        for a, b in zip(A, B): 
            if a == b:
                intersection_count += 1            
            if a in seen_b:
                intersection_count += 1
            if b in seen_a:
                intersection_count += 1
                        
                        
            seen_a.add(a)
            seen_b.add(b)
            
            c.append(intersection_count)
        
        return c
            
            