class Solution:
    def transform(self, word):
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code = []
        
        for char in word:
            code.append(morse_code[ord(char) - 97])
        
        return ''.join(code)
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = set()
        
        for word in words:
            morse_code = self.transform(word)
            codes.add(morse_code)
        
        return len(codes)
            
        