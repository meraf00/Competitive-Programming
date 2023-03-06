class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        first_elem = []        
                
        for index, item in enumerate(intervals):
            first, _ = item
            first_elem.append((first, index))
        
        first_elem.sort()
        
        output = []
        for _, second_elem in intervals:            
            index = bisect_left(first_elem, (second_elem, 0))
            
            if index >= len(intervals):
                index = -1
            else:                
                _, index = first_elem[index]
            output.append(index)
        
        return output
        