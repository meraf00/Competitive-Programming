"""
https://leetcode.com/problems/boats-to-save-people/
"""

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            if left == right:
                boats += 1
                break                
            if people[left] == limit:
                boats += 1
                left += 1
            elif people[right] == limit:
                boats += 1
                right -= 1
            elif people[left] + people[right] <= limit:
                left += 1
                right -= 1
                boats += 1
            elif people[left] + people[right] > limit:
                right -= 1
                boats += 1
        
        return boats