class Solution:
                    
    def removeComments(self, source: List[str]) -> List[str]:
        output = []
        comment = False
        new_line = True
        for line in source:
            if not new_line:
                cleaned_line = list(output.pop())
            else:
                cleaned_line = []
                
            i = 0
            while i < len(line):
                if not comment and i + 1 < len(line) and line[i] == "/" and line[i+1] == "*":
                    comment = True
                    new_line = False
                    i += 2
                    continue
                
                if i + 1 < len(line) and line[i] == line[i+1] == "/" and not comment:                    
                        break
                    
                if comment and i + 1 < len(line) and line[i] == "*" and line[i+1] == "/":
                    i += 2
                    new_line = True
                    comment = False
                    continue
                    
                if not comment:
                    cleaned_line.append(line[i])   
                    
                i += 1
            
            to_str = "".join(cleaned_line)
            
            if len(to_str):
                output.append(to_str)
        return output
                    
            