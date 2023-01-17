class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:         
        for i in range(len(names)):  
            swap = False
            for j in range(len(names) - i - 1):
                leftHeight = heights[j]
                rightHeight = heights[j+1]
             
                if leftHeight < rightHeight:
                    swap = True
                    names[j], names[j+1] = names[j+1], names[j]
                    heights[j], heights[j+1] = heights[j+1], heights[j]
            
            if not swap:
                return names
        
        return names
        