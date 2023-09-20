class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        zipped = sorted(zip(growTime, plantTime), reverse=True)
        
        total_pt = 0      
        total = 0
        for gt, pt in zipped:
            total_pt += pt            
            total = max(total_pt + gt, total)
            
        
        return total
            