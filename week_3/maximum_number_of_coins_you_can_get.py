from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)        
        
        myIndex = 1
        bobIndex = len(piles) - 1
        
        mySum = 0
        while bobIndex > myIndex:
            mySum += piles[myIndex]
            bobIndex -= 1
            myIndex += 2
            
        return mySum        