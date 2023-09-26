class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda: None)
        self.is_end = False            

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        current = self.root
        
        for char in word:                        
            if not current.children[char]:
                current.children[char] = TrieNode()
            
            current = current.children[char]
                        
        current.is_end = True
                    
    def search(self, word: str, root = None) -> bool:        
        if root == None:
            current = self.root 
        
        else:
            current = root
                
        for i, char in enumerate(word):
            if char == '.':                
                for child in current.children.values():
                    if child and self.search(word[i + 1:], child):                        
                        return True
                                
                return False
                        
            if not current.children[char]:                
                return False
            
            current = current.children[char]
        
        return current.is_end
    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)