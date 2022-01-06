from typing import List

class Solution:
    
    def countSwaps(self, a: List) -> None:        
        n = len(a)

        counter = 0

        for i in range(n):
            for j in range(n-1):
                
                if a[j] > a[j + 1]:
                    temp = a[j + 1]
                    a[j + 1] = a[j]
                    a[j] = temp
                    counter += 1
        
        print (f"Array is sorted in {counter} swaps.")
        print (f"First Element: {a[0]}")
        print (f"Last Element: {a[-1]}")

Solution().countSwaps([4,6,1])
