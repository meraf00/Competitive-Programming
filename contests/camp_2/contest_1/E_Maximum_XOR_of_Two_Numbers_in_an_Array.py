class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = -1

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        current = self.root                
        
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            
            if bit not in current.children:
                current.children[bit] = TrieNode()
        
            current = current.children[bit]
                    
        current.value = num        
    
    def maximize_xor(self, num):
        current = self.root                
        
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            
            opposite = bit ^ 1                        
                                    
            if opposite in current.children:
                current = current.children[opposite]
            
            else:
                current = current.children[bit]                
                
        return num ^ current.value

test_cases = int(input())

for _ in range(test_cases):
    input()
    nums = list(map(int, input().split()))

    trie = Trie()
            
    for num in nums:
        trie.insert(num)
        

    max_xor = 0

    for num in nums:            
        max_xor = max(trie.maximize_xor(num), max_xor)

    print(max_xor)
