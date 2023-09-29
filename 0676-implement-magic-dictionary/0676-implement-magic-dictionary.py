class TrieNode:
    def __init__(self):
        self.children = {}        
        self.is_end = False
        self.word_count = 0


class MagicDictionary:

    def __init__(self):
        self.pattern_root = TrieNode()    
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
                
            current = current.children[char]
                
        current.is_end = True
        
    def insert_pattern(self, pattern):
        current = self.pattern_root
        
        for char in pattern:
            if char not in current.children:
                current.children[char] = TrieNode()
                
            current = current.children[char]
        
        current.word_count += 1
        current.is_end = True

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.insert(word)
            
            for i in range(len(word)):
                self.insert_pattern(word[:i] + '*' + word[i+1:]) 
    
    def search_word(self, word):
        current = self.root
        
        for char in word:
            if char not in current.children:                
                return False
            
            current = current.children[char]
        
        return current.is_end
    
    def search_pattern(self, pattern, word_exists=False):
        current = self.pattern_root
        
        for char in pattern:
            if char not in current.children:                
                return False
            
            current = current.children[char]
        
        if word_exists:
            return current.is_end and current.word_count > 1
        
        return current.is_end

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            if self.search_word(searchWord):
                if self.search_pattern(searchWord[:i] + "*" + searchWord[i+1:], True):
                    return True
            
            else:                
                if self.search_pattern(searchWord[:i] + "*" + searchWord[i+1:]):
                    return True
        
        return False
            
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)