class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    
    def insert_and_checkprefix(self, word):
        current  = self.root
                
        length = len(word)
        
        all_prefix_found = True
        
        for idx, char in enumerate(word):
            if char not in current.children:
                current.children[char] = TrieNode()
                        
            current = current.children[char]
            
            if idx < length - 1:
                all_prefix_found = all_prefix_found and current.is_end
            
        current.is_end = True        
        
        return all_prefix_found

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda word: (len(word), word))
        
        trie = Trie()        
        
        max_length = 0
        longest_word = ''
        
        for word in words:
            is_valid = trie.insert_and_checkprefix(word)
            
            word_length = len(word)
            
            if is_valid and word_length > max_length:
                longest_word = word
                max_length = word_length
        
        return longest_word