"""https://leetcode.com/problems/reverse-string-ii/"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = [c for c in s]

        i = -1
        for i in range(len(s) //  (2 * k)):
            st = 2 * i * k
            end = st + k - 1            
            while st < end:
                s[st], s[end] = s[end], s[st]
                st += 1
                end -= 1
        
        if len(s) % (2 * k) != 0:            
            st = 2 * k * (i + 1)            
            
            if len(s) -  st < k:
                end = len(s) -  1
            else:
                end = st + k - 1

            while st < end:
                s[st], s[end] = s[end], s[st]
                st += 1
                end -= 1

        return "".join(s)
