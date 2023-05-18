class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
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
            
            if rank[xRep] >= rank[yRep]:
                rep[yRep] = xRep
                rank[xRep] += rank[yRep]
            
            else:
                rep[xRep] = yRep
                rank[yRep] += rank[xRep]
            
        
        unequals = []
        for equation in equations:
            a = equation[0]
            operator = equation[1]
            b = equation[3]
            
            if a not in rep:
                rep[a] = a
            
            if b not in rep:
                rep[b] = b
            
            if operator == "=":
                union(a, b)
            
            else:
                unequals.append((a, b))
        
        for a, b in unequals:
            if find(a) == find(b):
                return False
        
        return True
            
            