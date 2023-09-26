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
        
    def dfs(self, root, suggestions, completion = None):
        if len(suggestions) == 3:
            return
        
        if completion == None:
            completion = []
                
        if root.is_end:
            suggestions.append(''.join(completion))            
            
        for i in range(26):
            if root.children[i]:
                char = chr(i + ord('a'))
                
                completion.append(char)
                
                self.dfs(root.children[i], suggestions, completion)
                
                completion.pop()
            
    
    def autocomplete(self, prefix, length):
        current = self.root
        
        for idx in range(length):
            i = ord(prefix[idx]) - ord('a')
            
            if not current.children[i]:
                return []
            
            current = current.children[i]
        
        suggestions = []                
                
        self.dfs(current, suggestions)
        
        return list(map(lambda x: prefix[:length] + x,  suggestions))
            

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        
        for product in products:
            trie.insert(product)
        
        
        suggestions = []
        
        for i in range(len(searchWord)):
            suggestion = trie.autocomplete(searchWord, i + 1)
            suggestions.append(suggestion)
        
        return suggestions
        
        
        
        
        
        