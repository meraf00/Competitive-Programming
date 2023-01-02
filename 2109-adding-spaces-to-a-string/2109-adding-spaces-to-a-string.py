class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = []
        
        index = 0
        num_spaces = len(spaces)
        for i, char in enumerate(s):
            if index < num_spaces and i == spaces[index]:
                output.append(" ")            
                index += 1
                
            output.append(char)
        
        return "".join(output)
            
        