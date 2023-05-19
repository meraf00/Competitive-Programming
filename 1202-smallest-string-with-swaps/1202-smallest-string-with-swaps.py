class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        length = len(s)
        
        rep = {i : i for i in range(length)}
        
        rank = [1] * length
        
        def find(node):
            parent = node
            while parent != rep[parent]:
                parent = rep[parent]
            
            while node != rep[node]:
                temp = rep[node]
                rep[node] = parent
                node = temp
            
            return parent
                
        
        def union(x, y):
            xRep = find(x)
            yRep = find(y)
            
            
            if rank[xRep] >= rank[yRep]:
                rep[yRep] = xRep
                rank[xRep] += rank[yRep]
            
            else:
                rep[xRep] = yRep
                rank[yRep] += rank[xRep]
            
        
        for a, b in pairs:
            union(a, b)
                    
            
        
        chars = defaultdict(list)
        indices = defaultdict(list)
        
        for idx in range(length):
            idxRep = find(idx)
            heappush(chars[idxRep], s[idx])
            heappush(indices[idxRep], idx)
        
        
        answer = [None] * length
        
        for idx in chars.keys():
            while chars[idx]:
                char = heappop(chars[idx])
                char_idx = heappop(indices[idx])
                answer[char_idx] = char
            
    
        return "".join(answer)
        