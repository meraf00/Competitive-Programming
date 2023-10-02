class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        colors += ' '
        
        left = 0
        
        removable_count = {
            'A': 0,
            'B': 0
        }
        
        for right in range(len(colors)):
            if colors[right] != colors[left]:
                char = colors[left]
                
                if right - left - 2 > 0:
                    removable_count[char] += right - left - 2
            
                left = right
            
        return removable_count['A'] > removable_count['B']
            
            