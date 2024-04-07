class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]                   
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        
        for char in reversed(word):
            i = ord(char) - ord('a')
            
            if not current.children[i]:
                current.children[i] = TrieNode()
                        
            current = current.children[i]
            
    
    
    def count_length(self):
        counter = 0
        leaf_count = 0
        
        def dfs(node, length): 
            nonlocal counter, leaf_count
            
            is_leaf = True
            for nbr in node.children:
                if nbr:
                    is_leaf = False
                    dfs(nbr, length + 1)
            
            if is_leaf:
                counter += length
                leaf_count += 1
            
        
        dfs(self.root, 0)
        
        return counter + leaf_count
        

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        
        for word in words:
            trie.insert(word)   
                
        return trie.count_length()
        
        
        