class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen_char_indices = {}        
        
        for current_index, char in enumerate(s):
            char_number = ord(char) - 97
            
            if char in seen_char_indices:
                actual_distance = current_index - seen_char_indices[char] - 1
                if distance[char_number] != actual_distance:
                    return False
            else:
                seen_char_indices[char] = current_index
                
        return True
                
        