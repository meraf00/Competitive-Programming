class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_index = -1
        self.is_end = False
    
class WordFilter:

    def __init__(self, words: List[str]):        
        self.root = TrieNode()
        
        for idx, word in enumerate(words):
            for i in range(len(word)):                
                self.insert(f'{word[i:]}/{word}', idx)
    
    def insert(self, word, word_index):
        current = self.root
        
        for char in word:                        
            if char not in current.children:
                current.children[char] = TrieNode()
            
            current = current.children[char]
        
        current.word_index = word_index
        
        current.is_end = True
        
        
    def f(self, pref: str, suff: str) -> int:                
        word = f'{suff}{"/"}{pref}'
        
        current = self.root
        
        for char in word:                        
            if char not in current.children:
                return -1
            
            current = current.children[char]                
        
        
        largest_idx = -1
        
        stack = [current]
        
        while stack:
            node = stack.pop()
            
            if node.is_end:
                largest_idx = max(largest_idx, node.word_index)
            
            for child in node.children.values():                
                stack.append(child)
        
        return largest_idx
            

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)