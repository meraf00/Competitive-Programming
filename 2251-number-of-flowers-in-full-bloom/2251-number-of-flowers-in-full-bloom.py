class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = len(flowers)
        
        flowers.sort()  
        
        flowers_copy = flowers[:]
        
        flowers_copy.sort(key = lambda x: (x[1], x[0]))                
        
        ans = []                
        
        for person in people:
            right = bisect_right(flowers, person, key=lambda x: x[0])
            
            left = bisect_left(flowers_copy, person, key=lambda x:x[1])
                                                                                
            ans.append(right - left)
                
        return ans

    
"""
[[1,6],[3,7],[9,12],[4,13]]
[2,3,7,11]
[[1,10],[3,3]]
[3,3,2]
[[19,37],[19,38],[19,35]]
[6,7,21,1,13,37,5,37,46,43]
[[21,34],[17,37],[23,43],[17,46],[37,41],[44,45],[32,45]]
[31,41,10,12]
"""