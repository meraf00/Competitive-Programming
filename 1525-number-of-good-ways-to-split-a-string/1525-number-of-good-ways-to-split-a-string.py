class Solution:
    def numSplits(self, s: str) -> int:
        left = defaultdict(int)
        right = defaultdict(int)
        
        for char in s:
            right[char] += 1
            
        
        count = 0
        for char in s:            
            left[char] += 1
            
            right[char] -= 1
            
            if right[char] <= 0:
                right.pop(char)
            
            if len(left) == len(right):
                count += 1
        
        return count