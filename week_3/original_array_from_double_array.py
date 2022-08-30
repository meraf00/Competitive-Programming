from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:         
        counter = {}
        
        for num in changed:
            if counter.get(num) == None:
                counter[num] = 1
            else:
                counter[num] += 1
        
        output = []
        
        freq_of_0 = counter.get(0)
        if freq_of_0:
            if (freq_of_0 % 2 != 0):
                return []
            else:
                output = [0] * (freq_of_0 // 2)        
                del counter[0]     
        
        for key in sorted(counter.keys()):              
            if counter.get(key * 2) == None:
                if counter[key] == 0:
                    continue
                return []
            
            if counter[key] <= counter[key*2]:       
                counter[key*2] -= counter[key]                
                output.extend([key] * counter[key])
            else:                
                return []
        return output