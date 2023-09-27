class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word_count = 0
        self.is_end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:            
            if char not in current.children:
                current.children[char] = TrieNode()
            
            current = current.children[char]
            
            current.word_count += 1

        current.is_end = True                

    def count_match(self, word):
        current = self.root

        max_length = 0

        for length, char in enumerate(word):
            current = current.children[char]

            if current.word_count > 1:
                max_length = length + 1

        
        return max_length

n = int(input())

trie = Trie()

words = []

for _ in range(n):
    word = input()
    trie.insert(word)
    words.append(word)


for word in words:
    print(trie.count_match(word))