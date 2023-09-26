class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
    

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        
        for char in word:
            i = ord(char) - ord('a')
            
            if not current.children[i]:
                current.children[i] = TrieNode()
            
            current = current.children[i]
            
        current.is_end = True
    
    
    def find_root(self, word):
        current = self.root
        
        for idx, char in enumerate(word):
            i = ord(char) - ord('a')
            
            if current.is_end:
                return word[:idx]
            
            if not current.children[i]:
                return word
            
            current = current.children[i]
        
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
            
        
        result = []
        
        for word in sentence.split(' '):
            root = trie.find_root(word)            
            result.append(root)
        
        return ' '.join(result)
        
        
        
            
            
            
            
            
            
            
            
            
                