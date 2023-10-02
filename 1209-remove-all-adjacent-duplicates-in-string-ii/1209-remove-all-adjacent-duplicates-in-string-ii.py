class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if not stack:
                stack.append((char, 1))
                continue
                
            prev_char, count = stack[-1]
            
            if prev_char == char:
                if count + 1 == k:
                    stack.pop()
                else:
                    stack[-1] = (char, count + 1)
            
            else:
                stack.append((char, 1))
        
        return ''.join(map(lambda x: x[0] * x[1], stack))