class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        
        ordered = []
        
        for char in order:
            if char not in counter:
                continue
                
            count = counter[char]
            
            ordered.append(char * count)
            
            counter.pop(char)
        
        for char, count in counter.items():
            ordered.append(char * count)
        
        
        return "".join(ordered)
            