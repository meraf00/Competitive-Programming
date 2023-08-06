class Solution:
    def balancedStringSplit(self, s: str) -> int:
        window_count = {'L': 0, 'R': 0}                
        
        answer = 0
        
        for right, char in enumerate(s):
            window_count[char] += 1
            
            if window_count['L'] == window_count['R']:
                answer += 1                
                window_count = {'L': 0, 'R': 0}
        
        
        return answer
                                
        