class Solution:    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n_cities = len(isConnected)
        
        reps = {i:i for i in range(1, n_cities + 1)}
        rank = {i:1 for i in range(1, n_cities + 1)}
        
        def find(city):            
            root = city
            while root != reps[root]:
                root = reps[root]
               
            while city != root:
                parent = reps[city]
                reps[city] = root
                city = parent
                               
            return root
       
        def union(x, y):
            rep_x = find(x)
            rep_y = find(y)
            
            if rep_x == rep_y:
                return
            
            if rank[rep_x] >= rank[rep_y]:
                reps[rep_y] = rep_x  
                rank[rep_x] += rank[rep_y]
                        
            else:
                reps[rep_x] = rep_y     
                rank[rep_y] += rank[rep_x]
            
           
        for row in range(n_cities):
            for col in range(n_cities):
                if isConnected[row][col]:
                    union(row + 1, col + 1)
                    
        unique_reps = set()
        
        for city in reps.keys():
            unique_reps.add(find(city))

        return len(unique_reps)
        