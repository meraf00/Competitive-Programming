class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:            
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:            
            if char not in current.children:
                return False

            current = current.children[char]

        return current.is_end_of_word

n_req = int(input())

names = {}
original = {}
trie = Trie()

for _ in range(n_req):
    old, new = input().split()

    if trie.search(new):     
        continue

    trie.insert(old)
    trie.insert(new)

    if old in names:
        original[names[old]] = new
        names[new] = names[old]
        names.pop(old)
    
    else:
        original[old] = new
        names[new] = old
        

print(len(original))

for old, new in original.items():
    print(old, new)
    
