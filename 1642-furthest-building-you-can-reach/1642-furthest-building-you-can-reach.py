class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:           
        using_ladder = []
        using_brick = [] 
        
        used_bricks = 0        
        i = 0    
        for i in range(1, len(heights)):
            height_diff = heights[i] - heights[i - 1]                        
            
            if height_diff > 0:                                                  
                heappush(using_brick, -height_diff)
                
                used_bricks += height_diff
                
                temp = heappop(using_brick)
                
                used_bricks += temp
                
                heappush(using_ladder, -temp)                                
                
                if len(using_ladder) > ladders:
                    temp = heappop(using_ladder)
                                                            
                    heappush(using_brick, -temp)
                    
                    used_bricks += temp
                
                if used_bricks > bricks or len(using_ladder) > ladders:
                    return i - 1
        return i
                    
                    
                    
                                           
        
            
            