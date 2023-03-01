class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        
        baskets = {}
        
        max_fruits = 0
        
        for right, fruit_type in enumerate(fruits):
            
            if fruit_type in baskets:
                baskets[fruit_type] += 1
                
            else:
                baskets[fruit_type] = 1
            
            while len(baskets) > 2:
                fruit_to_remove = fruits[left]
                
                baskets[fruit_to_remove] -= 1
                
                if baskets[fruit_to_remove] == 0:
                    del baskets[fruit_to_remove]
                
                left += 1
                        
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits
            
            
            
        