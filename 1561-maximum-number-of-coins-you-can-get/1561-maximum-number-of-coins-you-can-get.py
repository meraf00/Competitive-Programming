class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        
        large_coins = len(piles) - 2
        small_coins = 0
                
        
        my_collection = 0
        while large_coins > small_coins:
            my_collection += piles[large_coins]
            large_coins -= 2
            small_coins += 1
        
        return my_collection