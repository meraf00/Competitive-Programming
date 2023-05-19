class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        length = len(source)
        
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
            
        
        for a, b in allowedSwaps:
            union(a, b)
            
        
        group = defaultdict(lambda : defaultdict(int))
        
        for i in range(length):
            indexRep = find(i)
            group[indexRep][source[i]] += 1
        
        
        hamming_distance = 0
        
        for idx, n in enumerate(target):
            indexRep = find(idx)
            
            if group[indexRep][n] <= 0:
                hamming_distance += 1
            
            group[indexRep][n] -= 1
            
        
        return hamming_distance
        