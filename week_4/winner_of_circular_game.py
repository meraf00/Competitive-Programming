"""
https://leetcode.com/problems/find-the-winner-of-the-circular-game/
"""

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k -= 1
        people = list(range(1, n + 1))
        i = k
        while len(people) > 1:            
            del people[i]
            i = (i + k) % len(people)
            
        return people[0]