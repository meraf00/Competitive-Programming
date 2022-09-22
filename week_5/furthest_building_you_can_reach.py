"""
https://leetcode.com/problems/furthest-building-you-can-reach/
"""


from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # top jumps 
        heap = []          # to be passed by ladder
              
        passed_by_brick = 0
        
        for i, height in enumerate(heights):            
            if i == len(heights) - 1:
                break
            
            if heights[i + 1] <= height:
                continue
            
            jump = heights[i + 1] - height
            
            # choose to use ladders for the largest jumps 
            if len(heap) < ladders:                
                heapq.heappush(heap, jump)
            
            # found new large jump 
            elif heap and jump > heap[0]:
                # so transfer old jump from ladder to brick and add new jump to ladder
                if passed_by_brick + heap[0] <= bricks:
                    passed_by_brick += heapq.heappop(heap)                                
                    heapq.heappush(heap, jump)
                
                # transfer is not possible b/c we don't have enough brick, also ladder
                else:
                    break
            
            # smaller jump so not eligible for ladder, use brick
            elif passed_by_brick + jump <= bricks:                
                passed_by_brick += jump
            
            # when we run out of brick / ladder
            else:                
                break
                        
        return i