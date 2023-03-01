class Solution:
    def simplifyPath(self, path: str) -> str:
        path = list(filter(lambda item: len(item) > 0, path.split("/")))
        
        stack = []
        
        for folder in path:
            if folder == "..":
                if stack:
                    stack.pop()
                continue
                
            elif folder == ".":
                continue
                
            stack.append(folder)
        
        return "/" + "/".join(stack)
        
            
        
        
        