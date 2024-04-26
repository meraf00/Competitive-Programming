class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # longest ending in letter        
        ending_letters = [0] * 26                
        
        for char in s:
            i = ord(char) - ord('a')
            
            temp = 0
            for j in range(max(i - k, 0), min(i + k + 1, 26)):
                temp = max(temp, ending_letters[j])
                
            ending_letters[i] = temp + 1

        return max(ending_letters)
            
            
            
        
        
        