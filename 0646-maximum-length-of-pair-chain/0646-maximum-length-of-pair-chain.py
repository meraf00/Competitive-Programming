class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:            
        pairs.sort(key=lambda x: x[1])
        
        chain_end = float('-inf')
        chain_length = 0
        
        for start, end in pairs:
            if start > chain_end:
                chain_length += 1
                chain_end = end
        
        return chain_length