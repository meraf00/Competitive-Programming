class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        target = len(candyType) // 2 
        
        unique_candies_count = len(set(candyType))
        
        return min(unique_candies_count, target)
        
        
            