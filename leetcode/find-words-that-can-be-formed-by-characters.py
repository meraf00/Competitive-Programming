class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_bank = Counter(chars)
        
        count = 0
        for word in words:
            required = Counter(word)
            
            for char in word:
                if required[char] > char_bank[char]:
                    break
            else:
                count += len(word)
                    
        return count