class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        n_cabels = len(connections)
        
        if n_cabels + 1 < n:
            return -1
        
        reps = [i for i in range(n)]
        ranks = [1] * n
        
        
        def find(member):
            root = member
            while reps[root] != root:
                root = reps[root]
                
            while reps[member] != root:
                parent = reps[member]
                reps[member] = root
                member = parent
            
            return root
        
        def union(x, y):
            xRep = find(x)
            yRep = find(y)
            
            if xRep == yRep:
                return 
                        
            if ranks[xRep] > ranks[yRep]:
                reps[yRep] = xRep
                ranks[xRep] += ranks[yRep]
            
            else:
                reps[xRep] = yRep
                ranks[yRep] += ranks[xRep]
        
        
        for a, b in connections:
            union(a, b)
        
        
        components = set()
        
        for computer in range(n):
            rep = find(computer)
            components.add(rep)
        

        return len(components) - 1
        
        
            
            