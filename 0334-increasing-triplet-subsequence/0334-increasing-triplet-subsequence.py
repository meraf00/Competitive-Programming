# [20,100,10,12,5,13]
# [0,4,2,1,0,-1,-3]
# [1,2,3,4,5]
# [5,4,3,2,1]
# [2,1,5,0,4,6]
# [6,4,3,7,5,8,2]
# [6,7,3,4, 1,2]
# [0,4,2,1,0,-1,-3]
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        i = None        
        j = None
        
        for k in nums:                            
            
            if i == None:
                i = k
            
            elif j == None and k > i:
                j = k
                
            elif k < i:
                i = k
                
            elif j != None and i < k < j :
                j = k
            
            elif j != None and k > j:
                return True                        
                
        return False