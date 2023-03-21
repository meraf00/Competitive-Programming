class Solution:
    def filter_valid(self, strings):        
        output = []
        for string in strings:
            unique, length = set(string), len(string)
            
            if len(unique) == length:
                output.append(unique)
            
        
        return output
            
    def maxLength(self, arr: List[str]) -> int:
        
        arr = self.filter_valid(arr)
        
        length = len(arr)
        
        max_length = 0
        
        current = []
        
        seen = set()
        
        def backtrack(index):
            nonlocal max_length, seen
            
            if index >= length:
                return
            
            for i in range(index, length):
                
                if len(seen.intersection(arr[i])) != 0:
                    continue
                    
                current.append(arr[i])
                
                seen = seen.union(arr[i])
                
                max_length = max(len(seen), max_length)
                
                backtrack(i + 1)
                
                last = current.pop()
                
                seen = seen - set(last)
                
        backtrack(0)
        
        return max_length
        