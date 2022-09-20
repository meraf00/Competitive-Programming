"""
https://leetcode.com/problems/pancake-sorting/
"""

from typing import List

class Solution:
    def flip(self, arr: List[int], left: int, right: int) -> None:        
        while left < right: 
            arr[left], arr[right] = arr[right], arr[left]
            return self.flip(arr, left + 1, right - 1)
        
    def pancakeSort(self, arr: List[int]) -> List[int]:        
        output = []
        for i in range(len(arr)):
            max_index = 0
            j = 0
            while j < len(arr) - i:
                if arr[j] > arr[max_index]:
                    max_index = j
            
                j += 1            
            if max_index != 0:            
                self.flip(arr, 0, max_index)
                output.append(max_index + 1)
                
            self.flip(arr, 0, len(arr) - i - 1)
            output.append(len(arr) - i)
        
        return output