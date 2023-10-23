class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cipher = {}
        
        letters = set('abcdefghijklmnopqrstuvwxyz')
        
        i = 0
        for char in key:
            if char in letters and char not in cipher:
                cipher[char] = chr(ord('a') + i)
                i += 1                
        
        res = []
                
        for char in message:
            if char in cipher:
                res.append(cipher[char])
            
            else:
                res.append(char)
        
        return ''.join(res)