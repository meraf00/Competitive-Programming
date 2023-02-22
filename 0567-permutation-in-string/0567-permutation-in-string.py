class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        
        left = 0
                
        window_size = len(s1)
        
        for right in range(len(s2)):
            current_char = s2[right]
            
            if freq.get(current_char):
                freq[current_char] -= 1
            
            elif current_char in freq:
                while freq[current_char] == 0:
                    freq[s2[left]] += 1
                    left += 1
                    
                freq[current_char] -= 1
            
            else:
                while left < right:
                    freq[s2[left]] += 1
                    left += 1
                left += 1
            
            if window_size == right - left + 1:
                return True
        
        return False