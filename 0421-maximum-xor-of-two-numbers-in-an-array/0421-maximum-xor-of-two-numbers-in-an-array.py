class Solution:
    def findMaximumXOR(self, nums):   
        max_len = len(bin(max(nums))) - 2  
            
        trie = {}
        
        def insert(num):
            current = trie
            
            for i in range(max_len, -1, -1):
                bit = (num >> i) & 1   
                
                if bit not in current:                    
                    current[bit] = {}                    
                current = current[bit]
        
        for num in nums:
            insert(num)
                
        max_xor = 0
                        
        for num in nums:
            current = trie
            
            value = 0
        
            for i in range(max_len, -1, -1):
                bit = (num >> i) & 1

                opposite = bit ^ 1                                
                        
                if opposite in current:                    
                    current = current[opposite]
                    value <<= 1
                    value |= opposite
                    
                else:                                  
                    current = current[bit]
                    value <<= 1
                    value |= bit
            
            max_xor = max(num ^ value, max_xor)
             
        return max_xor
    
                
            