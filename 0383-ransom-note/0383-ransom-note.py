class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine)
        ransom_count = Counter(ransomNote)
        
        for letter in ransomNote:
            if ransom_count[letter] > magazine_count[letter]:
                return False
        
        return True
            