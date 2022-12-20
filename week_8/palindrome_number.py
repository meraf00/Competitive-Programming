"""https://leetcode.com/problems/palindrome-number/"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        init_x = x
        reversed_x = 0
        while x:
            last_dig = x % 10
            x //= 10
            reversed_x *= 10
            reversed_x += last_dig

        return reversed_x == init_x
