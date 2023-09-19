class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
                
        current = []
        counter = 0
        
        def backtrack(length):
            nonlocal counter
            
            if length == 0:
                counter += 1
                return
            
            for i in range(5):
                if not current:
                    current.append(vowels[i])
                    backtrack(length - 1)
                    current.pop()
                
                elif vowels[i] >= current[-1]:
                    current.append(vowels[i])
                    backtrack(length - 1)
                    current.pop()
                            
        backtrack(n)
        
        return counter