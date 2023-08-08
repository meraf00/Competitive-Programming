class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        
        return -1
        