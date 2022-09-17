"""
https://codeforces.com/problemset/problem/768/B
"""

from functools import lru_cache
from typing import List, Tuple

class Solution:

    #3rd attempt
    def decomposed_size(self, n: int) -> int:
        """Returns the length of digits a number will have when decomposed"""
        i = 0
        while pow(2, i) < n:
            i += 1        
        
        return pow(2, i) - 1

    def decompose_once(self, n: int) -> int:  
        if n <= 1:
            return n

        return [n // 2, n % 2, n // 2]
    
    def code_for_one(self, decomposed: List[int], start: int, end: int) -> int:                 
        start -= 1
        end -= 1

        while start != 0 and end != len(decomposed) - 1: 
            print(decomposed, start, end)           
            i = 0
            eff_i = 0                   # effective index (index if all digits were expanded)
            left = right = None         # where to slice the decomposed list 
            while i < len(decomposed):
                digit = decomposed[i]
                size = self.decomposed_size(digit)
                eff_i += size
                i += 1

                if left == None and eff_i > start:
                    left = i
                if right == None and eff_i > end:
                    right = i
            
            eff_removed = 0                                
            for i, dig in enumerate(decomposed):                
                if i < left:                    
                    eff_removed += self.decomposed_size(dig)
                
                print(left, right, ">>", decomposed, i, dig, eff_removed)
            
            start -= eff_removed + 1
            end -= eff_removed + 1

            new = []
            i = left        
            while i <= right:
                if decomposed[i] <= 1:
                    new.append(decomposed[i])
                else:
                    new.extend(self.decompose_once(decomposed[i]))
                i += 1
            
            del decomposed
            
            decomposed = new            
        
        return decomposed

    # 2nd attempt [failed because it's memory intensive]
    """
    def decompose(self, n: int):        
        mids = []        
        while n > 1:                        
            mids.append(n % 2)
            n //= 2

        decomposed = [n]
        
        i = len(mids) - 1
        while i >= 0:
            decomposed.append(mids[i])
            decomposed.extend(decomposed[:len(decomposed)-1])
            i -= 1
        return decomposed

    def code_for_one(self, n: int, start: int, end: int) -> int:          
        counter = 0
        for i in self.decompose(n)[start - 1 : end]:
            if i == 1:
                counter += 1
        return counter
    """

    # First trial failed recursion limit
    """
    @lru_cache(maxsize=None)    
    def find_undecomposed(self, list_: Tuple[int]) -> bool:        
        for i, digit in enumerate(list_):
            if digit != 0 and digit != 1:                
                return i
        return -1

    @lru_cache(maxsize=None)
    def decompose(self, digits: Tuple[int]) -> Tuple[int]:  
        undecomposed = self.find_undecomposed(digits)
        if undecomposed == -1:
            return tuple(digits)
        
        new = []
        replacement = [digits[undecomposed] // 2, digits[undecomposed] % 2, digits[undecomposed] // 2]
        i = 0
        while i < len(digits):
            if i == undecomposed:
                new.extend(replacement)
            else:
                new.append(digits[i])
            i += 1
        
        return self.decompose(tuple(new))

    def code_for_one(self, n: int, start: int, end: int) -> int:  
        print(self.decompose((n,))    )
        counter = 0
        for i in self.decompose((n,))[start - 1 : end]:
            if i == 1:
                counter += 1
        return counter
    """


# take input
n, start, end = 7, 4, 5#list(map(int, input().strip().split(" ")))

print(Solution().code_for_one([n], start, end))

