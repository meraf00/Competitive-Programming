class TrieNode:
    def __init__(self, char=''):
        self.children = {}
        self.is_end = False
        self.char = char
    
    def __repr__(self):
        return f'<{self.char}{"!" if self.is_end else ""}>'

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode(char)
            
            current = current.children[char]
        
        current.is_end = True        
        

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        for word in words:
            self.trie.insert(word)
        
        self.nodes = set()
        

    def query(self, letter: str) -> bool:
        found_suffix = False
        
        nodes_to_remove = [] 
        nodes_to_add = []
        
        for node in self.nodes:
            if letter in node.children:                
                nodes_to_add.append(node.children[letter])
                
                found_suffix = found_suffix or node.children[letter].is_end
            
            nodes_to_remove.append(node)
        
        for node in nodes_to_remove:
            self.nodes.remove(node)
        
        self.nodes.update(nodes_to_add)                
                
        if letter in self.trie.root.children:
            self.nodes.add(self.trie.root.children[letter])
            found_suffix = found_suffix or self.trie.root.children[letter].is_end
                
        return found_suffix
                    
        
            
            
                
                
            
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)