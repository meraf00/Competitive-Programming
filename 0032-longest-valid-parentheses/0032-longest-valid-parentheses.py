class Solution:
    def longestValidParentheses(self, s: str) -> int:
        valid_map = defaultdict(int)
        
        stack = []
        
        max_length = 0
        
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            
            elif stack:
                open_idx = stack.pop()
                
                length = idx - open_idx + 1                
                
                length += valid_map[open_idx - 1]
                
                valid_map[idx] = length
                
            max_length = max(valid_map[idx], max_length)
                
            
        return max_length