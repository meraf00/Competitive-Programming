class TrieNode:
    def __init__(self) -> None:
        self.children: list[TrieNode | None] = [None for _ in range(26)]
        self.word_count = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            idx = ord(char) - ord('a')

            if not current.children[idx]:
                current.children[idx] = TrieNode()

            current = current.children[idx]

        current.word_count += 1

    def count_word(self, word: str) -> int:
        current = self.root                
        
        for char in word:
            idx = ord(char) - ord('a')

            if not current.children[idx]:
                return 0

            current = current.children[idx]            

        return current.word_count
    
    
    def merge_child(self, parent, child, idx):
                
        if parent.children[idx] == None:             
            parent.children[idx] = child
            return
        
        parent.children[idx].word_count += child.word_count
        
        for c_idx, c in enumerate(child.children):
            if c:                
                self.merge_child(parent.children[idx], c, c_idx)            
        
    
    def remove_prefix(self, prefix: str) -> None:
        current = self.root                 
        
        for char in prefix:
            idx = ord(char) - ord('a')
            
            if not current.children[idx]:
                return
            
            current = current.children[idx]
        
        i = ord(prefix[0]) - ord('a')
        
        self.root.children[i] = None
        
        for idx, child in enumerate(current.children):
            if child:
                self.merge_child(self.root, child, idx)
            

    def has_prefix(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            idx = ord(char) - ord('a')

            if not current.children[idx]:
                return False

            current = current.children[idx]

        return True

    
class Solution:            
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        count = 0
        
        for char in s:
            n_words = trie.count_word(char)
            
            
            count += n_words
            
            trie.remove_prefix(char)            
        
        return count
        
        
            
            
"""
"abcdea"
["aca","bac"]
"abcde"
["a","bb","acd","ace"]
"dsahjpjauf"
["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
"qlhxagxdqh"
["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]
"""            
        
        
        