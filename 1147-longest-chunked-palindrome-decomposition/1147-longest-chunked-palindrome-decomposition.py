class Solution:
    def longestDecomposition(self, text: str) -> int:        
        def longest(left, right):
            if left > right:
                return 0
            
            for i in range(1, right - left + 1):
                if text[left:left+i] == text[right-i+1:right+1]:
                    return 2 + longest(left+i, right-i)                    
        
            return 1
        
        return longest(0, len(text)-1)