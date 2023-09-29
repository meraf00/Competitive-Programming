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
            idx = ord(char) - ord('a')
            
            if not current.children[idx]:
                current.children[idx] = TrieNode()
        
            current = current.children[idx]
        
        current.is_end = True
                
    
    def search(self, word):
        current = self.root
        
        for char in word:
            idx = ord(char) - ord('a')
            
            if not current.children[idx]:
                return False
        
            current = current.children[idx]
        
        return current.is_end
        

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        length = len(s)
        
        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
        
        # min extra character when splitting s[:i]
        dp = [float('inf')] * (length + 1)
        dp[0] = 0
        
        for i in range(1, length + 1):            
            for j in range(i - 1, -1, -1):                                
                if trie.search(s[j:i]):
                    dp[i] = min(dp[j], dp[i])
                
                else:
                    dp[i] = min(dp[j] + i - j, dp[i])
                    
                    
        return dp[-1]
        
        
        
        
        
        
        
        
        
        
        
        