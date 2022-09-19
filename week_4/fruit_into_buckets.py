"""
https://leetcode.com/problems/fruit-into-baskets/
"""

from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        buckets = set()
        
        left = right = 0
        max_fruits = 0        
        
        while right < len(fruits): 
            # print(left, right, max_fruits, buckets)                
            
            if fruits[right] in buckets:
                max_fruits = max(max_fruits, right - left + 1)
                right += 1                
            
            elif fruits[right] not in buckets:                
                if len(buckets) >= 2:                       
                    for fruit in buckets:
                        if fruits[right - 1] != fruit:
                            fruit_to_remove = fruit
                            break
                    buckets.remove(fruit_to_remove)
                    buckets.add(fruits[right])
                    left = right
                    while left > 0 and fruits[left - 1] in buckets:
                        left -= 1
                else:
                    buckets.add(fruits[right])
                                        
                        
        return max_fruits