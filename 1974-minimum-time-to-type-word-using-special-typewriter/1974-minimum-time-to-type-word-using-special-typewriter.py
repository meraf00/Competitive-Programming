class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        
        char_map = {char: idx for idx, char in enumerate(string.ascii_lowercase)}
        
        current_idx = 0
        
        for target_char in word:
            target_idx = char_map[target_char]
                        
            clockwise_gap = (current_idx - target_idx) % 26
            counter_clockwise_gap = (target_idx - current_idx) % 26
            
            if clockwise_gap < counter_clockwise_gap:
                time += clockwise_gap + 1                
            
            else:
                time += counter_clockwise_gap + 1                
            
            current_idx = target_idx
        
        return time

            
            