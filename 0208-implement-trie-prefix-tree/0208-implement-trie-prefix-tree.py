class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end_of_word = False        


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if not current.children[idx]:
                current.children[idx] = TrieNode()
            
            current  = current.children[idx]
        
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        
        for char in word:
            idx = ord(char) - ord('a')
            
            if not current.children[idx]:
                return False
            
            current = current.children[idx]
        
        return current and current.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        
        for char in prefix:
            idx = ord(char) - ord('a')
            
            if not current.children[idx]:
                return False
            
            current = current.children[idx]
        
        return current != None
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)