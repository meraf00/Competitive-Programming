class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(map(lambda x: ord(x) - 97, s))
        
        length = len(s)
        prefix = [0] * length
        
        for start, end, direction in shifts:
            prefix[start] += 1 if direction else -1
            if end + 1 < length:
                prefix[end + 1] += -1 if direction else 1
        
        for i in range(1, length):
            prefix[i] += prefix[i-1]
        
        for i in range(length):
            s[i] = chr(((s[i] + prefix[i]) % 26) + 97)
        
        return "".join(s)
        
        
            