class Solution:  
    
    def clamp(self, value, minimum, maximum):
        if value < minimum:
            return minimum
        elif value > maximum:
            return maximum
        else:
            return value
        
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        
        r = 0
        c = 0
        
        output = []
        north_east = True
        
        while r < rows and c < cols:                        
            
            output.append(mat[r][c])
                        
            if north_east:
                new_r = r - 1
                new_c = c + 1
                
                if 0 <= new_r <= rows-1 and 0 <= new_c <= cols-1:
                    r = new_r
                    c = new_c
                
                elif new_r < 0:
                    if new_c < cols:
                        c = new_c
                    else:
                        r += 1
                    
                    north_east = not north_east 
                
                elif new_r > rows - 1:
                    c += 1
                    north_east = not north_east 
                
                elif new_c > cols - 1:
                    r += 1
                    north_east = not north_east 
                    
                
            else:
                new_r = r + 1
                new_c = c - 1
                
                if 0 <= new_r <= rows-1 and 0 <= new_c <= cols-1:
                    r = new_r
                    c = new_c
            
                elif new_c < 0:
                    if new_r < rows:
                        r = new_r
                    else:
                        c += 1
                    
                    north_east = not north_east   
                
                elif new_c > cols - 1:
                    r += 1
                    north_east = not north_east 
                
                elif new_r > rows - 1:
                    c += 1
                    north_east = not north_east 
                            
        return output