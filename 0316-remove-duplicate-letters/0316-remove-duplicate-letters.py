class Solution:
    def removeDuplicateLetters(self, s: str) -> str:                
        
        last_indices = {}
        
        for index, char in enumerate(s):
            last_indices[char] = index
            
        
        stack = []
        seen = set()
        
        for index, char in enumerate(s):
            if char not in seen:
                while stack and stack[-1] > char and last_indices[stack[-1]] > index:
                    removed = stack.pop()
                    seen.remove(removed)
            
                stack.append(char)
                seen.add(char)


        return "".join(stack)