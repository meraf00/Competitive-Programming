class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reps = [i for i in range(n)]
        ranks = [1] * n    
        
        def find(x):
            root = x
            while reps[root] != root:
                root = reps[root]
            
            current = x
            while reps[current] != root:
                parent = reps[current]
                reps[current] = root
                current = parent
            
            return root
        
        
        def union(x, y):
            xRep = find(x)
            yRep = find(y)
            
            if ranks[xRep] < ranks[yRep]:
                reps[xRep] = yRep
                ranks[yRep] += ranks[xRep]
            else:                
                reps[yRep] = xRep
                ranks[xRep] += ranks[yRep]
            
                            
        for i, query in enumerate(queries):
            queries[i].append(i)
                
        edgeList.sort(key = lambda edge: edge[2])
        queries.sort(key = lambda q: q[2])
                
        
        n_edges = len(edgeList)
        edge_ptr = 0
        
        result = [False] * len(queries)        
        
        for p, q, limit, query_idx in queries:
            while edge_ptr < n_edges and edgeList[edge_ptr][2] < limit:
                u, v, _ = edgeList[edge_ptr]
                union(u, v)
                edge_ptr += 1
                                    
            result[query_idx] = find(p) == find(q)
            
            
        return result   