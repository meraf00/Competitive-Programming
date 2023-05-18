class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep = {}        
        rank = defaultdict(lambda: 1)
        
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
            
            if xRep != yRep:
                if rank[xRep] >= rank[yRep]:
                    rep[yRep] = xRep
                    rank[xRep] += rank[yRep]

                else:
                    rep[xRep] = yRep
                    rank[yRep] += rank[xRep]
                
        
        n_stones = len(stones)
        
        for i in range(n_stones):
            if i not in rep:
                rep[i] = i
                rank[i] = 1
                
            for j in range(i + 1, n_stones):
                x0, y0 = stones[i]
                x1, y1 = stones[j]                                
                
                if j not in rep:
                    rep[j] = j
                    rank[j] = 1
                    
                
                if abs(x0 - x1) == 0 or abs(y0 - y1) == 0:
                    # print(stones[i], stones[j])
                    union(i, j)

        components = set()
        
        for i in range(n_stones):
            components.add(find(i))
        
        count = 0
        
        for stone in components:
            count += rank[stone] - 1
        
        return count
            
        
        