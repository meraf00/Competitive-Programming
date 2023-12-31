class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_index = defaultdict(lambda : float('inf'))
        last_index = defaultdict(lambda : float('-inf'))
        
        max_len = -1
        
        for i, char in enumerate(s):
            first_index[char] = min(i, first_index[char])
            last_index[char] = max(i, last_index[char])
            
            max_len = max(max_len, last_index[char] - first_index[char] - 1)
        
        return -1 if max_len <= -1 else max_len
        
        
        