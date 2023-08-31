class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        def is_palindrome(s, left, right):                        
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
                
            return True
                                    
        
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            
            else:
                remove_left = is_palindrome(s, left + 1, right)
                remove_right = is_palindrome(s, left, right - 1)
                                
                if remove_left or remove_right:
                    return True
              
                else:
                    return False
                                
        return True

    
"""
"aba"
"abca"
"abc"
"caaccacac"
"adceceadbddbdaececrda"
"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
"""