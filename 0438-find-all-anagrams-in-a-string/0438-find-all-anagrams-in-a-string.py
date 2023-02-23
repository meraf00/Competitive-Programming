class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = Counter(p)
        
        left = 0
        
        result = []
        
        window_size = len(p)
        
        for right in range(len(s)):
            current_char = s[right]
            
            if freq.get(current_char):
                freq[current_char] -= 1
            
            elif current_char in freq:
                while freq[current_char] == 0:
                    freq[s[left]] += 1
                    left += 1
                    
                freq[current_char] -= 1
            
            else:
                while left < right:
                    freq[s[left]] += 1
                    left += 1
                left += 1
            
            if window_size == right - left + 1:
                result.append(left)
        
        return result
                
                