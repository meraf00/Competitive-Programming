class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()
        
        for word in words:
            letter_count = [0] * 52
            
            for idx, char in enumerate(word):                
                # odd
                if idx & 1:                    
                    letter_count[ord(char) - 97] += 1
                
                else:
                    letter_count[ord(char) - 71] += 1
            
            identifier = '_'.join(map(str, letter_count))
            
            groups.add(identifier)
        
        
        return len(groups)
                
            