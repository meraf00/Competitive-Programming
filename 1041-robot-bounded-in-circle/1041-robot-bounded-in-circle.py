class Solution:
    def isRobotBounded(self, instructions: str) -> bool:                   
        def rotate(d, r):
            rot = {
                'L': [[0, -1], [1, 0]],
                'R': [[0, 1], [-1, 0]]                
            }
            
            
            return (rot[r][0][0] * d[0] + rot[r][0][1] * d[1], 
                    rot[r][1][0] * d[0] + rot[r][1][1] * d[1])
            
        
        pos = (0, 0)
        dir = (0, 1)
        
        for ins in instructions:
            if ins == 'G':
                pos = (pos[0] + dir[0], pos[1] + dir[1])
            
            else:
                dir = rotate(dir, ins)
                
        
        if pos == (0, 0):
            return True
        
        if dir != (0, 1):
            return True
        
        return False
        
          
        
            