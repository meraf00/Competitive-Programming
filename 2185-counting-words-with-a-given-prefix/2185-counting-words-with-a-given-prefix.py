class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode | None] = defaultdict(lambda: None)
        self.word_count = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:            
            if not current.children[char]:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.word_count += 1

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:            
            if not current.children[char]:
                return False

            current = current.children[char]

        return current.word_count

    def count_words_with_prefix(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:            
            if not current.children[char]:
                return 0

            current = current.children[char]

        stack = [current]
        
        visited = set()
        
        count = 0
        
        while stack:
            current = stack.pop()
            
            visited.add(current)
            
            count += current.word_count                
            
            for child in current.children.values():
                if child not in visited:
                    stack.append(child)
        
        return count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        return trie.count_words_with_prefix(pref)
        
        
        
        
        
        
        
        
        
        
        
        
        