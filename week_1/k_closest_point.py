from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:  
                               
        points.sort(key=lambda e: e[0] ** 2 + e[1] ** 2 )
            
        return points[0:k]
            
            
