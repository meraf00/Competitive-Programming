class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, array, start, end):
        current = self.root
                
        for i in range(start, end + 1):
            num = array[i]
            
            if num not in current.children:
                current.children[num] = TrieNode()
            
            current = current.children[num]

        current.is_end = True
    
    def search(self, array, start, end):
        current = self.root
        
        for i in range(start, end + 1):
            num = array[i]                            
            
            if num not in current.children:
                return False
            
            current = current.children[num]
        
        return current.is_end                                    
                

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        length = len(nums)
                                
        subarray_count = 0                
        
        trie = Trie()
                        
        for i in range(length):
            
            divisible_count = 0
            
            for j in range(i, length):
                
                if nums[j] % p == 0:
                    divisible_count += 1
                
                if divisible_count > k:
                    break
                
                if not trie.search(nums, i, j):                    
                    trie.insert(nums, i, j)                    
                    subarray_count += 1                        
                
        return subarray_count
                
                