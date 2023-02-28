class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        
        longest = 0
        
        left = 0
        
        for right, char in enumerate(s): 
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
            
            max_freq = sorted(chars.values())[-1]
            
            window_size = right - left + 1
            
            to_be_replaced = window_size - max_freq
            
            # print(f"{chars=}, {max_freq=}, {window_size=}, {to_be_replaced=}, {longest=}, {left=}")
            
            while left < right and to_be_replaced > k:
                left_char = s[left]
                
                chars[left_char] = max(0, chars[left_char] - 1)
                
                left += 1
                
                max_freq = sorted(chars.values())[-1]
            
                window_size = right - left + 1

                to_be_replaced = window_size - max_freq
                        
            longest = max(longest, window_size)
        
        return longest
                        
            
                
            
                
            
        
        
        