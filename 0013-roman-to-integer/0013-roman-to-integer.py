class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        
        num = 0
        
        last = None
        
        for char in reversed(s):
            if last and roman_map[last] > roman_map[char]:
                num -= roman_map[char]
            
            else:
                num += roman_map[char]
            
            last =  char
        
        return num
            