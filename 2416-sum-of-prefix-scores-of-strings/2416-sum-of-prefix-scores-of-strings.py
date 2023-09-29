class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_count = 0
        self.is_end = False

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    
    def insert(self, word):
        current = self.root 
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
        
            current = current.children[char]
            current.word_count += 1
        
        current.is_end = True
    
    def count_prefix(self, word):
        current = self.root 
        
        count = 0
        for char in word:
            current = current.children[char]            
            count += current.word_count
        
        return count
        

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        
        prefix_count = []
        
        for word in words:            
            count = trie.count_prefix(word)
            
            prefix_count.append(count)
    
        return prefix_count
                
            
        