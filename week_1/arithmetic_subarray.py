from typing import List

class Solution:
    
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        
        for i in range(len(l)):
            subarray = sorted( nums[l[i] : r[i] + 1] )
            
            if len(subarray) > 1:            
                gap = subarray[0] - subarray[1]        
                
                arithmetic = True
                
                for j in range(len(subarray) - 1):
                    if subarray[j] - subarray[j+1] != gap:   
                        arithmetic = False
                        break      
                        
                answer.append(arithmetic)
                        
            else:
                answer.append(True)
        
        return answer
