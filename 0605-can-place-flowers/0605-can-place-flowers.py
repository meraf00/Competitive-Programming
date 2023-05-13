class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        EMPTY = 0
        PLANT = 1
        
        flowerbed.append(0)
        
        
        for i in range(len(flowerbed) - 1):
            if flowerbed[i] == EMPTY:
                if flowerbed[i - 1] == EMPTY and flowerbed[i + 1] == EMPTY:
                    flowerbed[i] = PLANT
                    n -= 1
        
        return n <= 0
        
        
        