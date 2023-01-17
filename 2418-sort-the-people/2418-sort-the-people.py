class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:   
        array_size = len(names)
        
        for i in range(array_size - 1):
            if heights[i] < heights[i + 1]:
                for j in range(i + 1, 0, -1):
                    if heights[j] < heights[j - 1]:
                        break
                        
                    names[j], names[j - 1] = names[j - 1], names[j]
                    heights[j], heights[j - 1] = heights[j - 1], heights[j]
            
                    
        return names
        