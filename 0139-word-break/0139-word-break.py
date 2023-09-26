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
    
    def search(self, word):
        current = self.root
        
        for char in word:
            i = ord(char) - ord('a')
            
            if not current.children[i]:
                return False
            
            current = current.children[i]
        
        return current.is_end
      
    def has_prefix(self, prefix):
        current = self.root
        
        for char in word:
            i = ord(char) - ord('a')
            
            if not current.children[i]:
                return False
            
            current = current.children[i]
        
        return True
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        
        for word in wordDict:
            trie.insert(word)
                
        length = len(s)        
        
        @cache
        def dp(idx):
            if idx >= length:
                return True
            
            for i in range(idx + 1, length + 1):
                word = s[idx:i]
                
                if trie.search(word):                     
                    if dp(i):
                        return True                    
                                
        return dp(0)        
        