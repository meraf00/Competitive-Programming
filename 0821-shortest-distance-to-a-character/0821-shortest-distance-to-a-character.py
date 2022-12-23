class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:  
        string_length = len(s)
        
        e_indices = []
        for idx, char in enumerate(s):
            if char == c:
                e_indices.append(idx)
        
        
        # pointers on e_indices
        left = -1
        right = 0
        
        output = [0] * string_length
        for char_idx, char in enumerate(s):            
            if char_idx >= e_indices[right]:
                left = min(len(e_indices) - 1, left + 1)
                right = min(len(e_indices) - 1, right + 1)                            
                
            distance_right = abs(char_idx - e_indices[right])            
            distance_left = abs(char_idx - e_indices[left])
            distance = min(distance_left, distance_right)                                                
                
            output[char_idx] = distance                            
        
        return output
            
            
                
        