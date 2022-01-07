class Solution:
    
    def countingValleys(self, path: str) -> int:
        elevation = 0
        valley = 0
        
        for p in path:
            if p == "D":
                if elevation == 0:
                    valley += 1                
                elevation -= 1
                
            else:
                elevation += 1
                
        return valley


