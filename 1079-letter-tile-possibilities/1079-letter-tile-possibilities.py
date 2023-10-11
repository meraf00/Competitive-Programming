class Solution:
    def numTilePossibilities(self, tiles: str) -> int:        
        n = len(tiles)                                
        
        seen = set()
        
        current = []
        
        used = set()
        
        def backtrack(i):
            if current:
                seen.add(''.join(current))                                        
            
            for j in range(n):
                if j != i and j not in used:
                    used.add(j)   
                    current.append(tiles[j])
                    backtrack(j)          
                    current.pop()
                    used.remove(j)
            
                                                        
        backtrack(-1)
        
        return len(seen)
            