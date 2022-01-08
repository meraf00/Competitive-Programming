from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dict_ = {}
        for num in arr:
            if num in dict_.keys():
                dict_[num] += 1
            else:
                dict_[num] = 1
        
        values = sorted(dict_.values(), reverse=True)
        
        target = len(arr) // 2
        
        counter = 0
        for v in values:
            if target > 0:            
                target -= v
                counter += 1

            else:
                break
                
        return counter
            
        
