class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_count = 0
        even_count = 0
        
        for n in position:
            if n & 1:
                odd_count += 1
            
            else:
                even_count += 1
        
        return min(odd_count, even_count)