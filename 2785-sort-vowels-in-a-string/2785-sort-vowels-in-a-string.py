class Solution:
    def sortVowels(self, s: str) -> str:
        letters = list(s)
        length = len(letters)
        
        vowels = set("aeiouAEIOU")
                
        
        found_vowels = []
        
        for letter in letters:
            if letter in vowels:
                found_vowels.append(letter)

        found_vowels.sort()
        
        
        if not found_vowels:
            return s
        
        next_vowel_idx = 0
        
        for i in range(len(letters)):
            if letters[i] in vowels:
                letters[i] = found_vowels[next_vowel_idx]
                next_vowel_idx += 1
            
        
        return "".join(letters)
    
        
        
                
            