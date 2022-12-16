"""https://leetcode.com/problems/valid-palindrome/"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for c in s:
            if c.isalnum():
                string.append(c.lower())

        for i in range(len(string) // 2):
            if string[i] != string[len(string) - i - 1]:
                return False
        return True
