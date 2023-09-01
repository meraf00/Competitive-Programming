class Solution:
    def are_equaivalent(self, s1, s2):            
            difference = []
            
            swapped = False
            
            for char1, char2 in zip(s1, s2):
                if char1 != char2:
                    if not difference:
                        difference.append(char1)
                        difference.append(char2)
                    
                    else:
                        if swapped:
                            return False
                        
                        if difference[0] == char2 and difference[1] == char1:
                            swapped = True
                        
                        else:
                            return False            
            return True
        
        
    def numSimilarGroups(self, strs: List[str]) -> int:
        n_strings = len(strs)
        
        reps = {s:s for s in strs}
        rank = {s: 1 for s in strs}
        
        def find(member):
            root = member
            while root != reps[root]:
                root = reps[root]
            
            while member != root:
                parent = reps[member]
                reps[member] = root
                member = parent
            
            return root
        
        
        def union(x, y):
            xRep = find(x)
            yRep = find(y)
            
            if rank[xRep] >= rank[yRep]:
                reps[yRep] = xRep
                rank[xRep] += rank[yRep]
            
            else:
                reps[xRep] = yRep
                rank[yRep] += rank[xRep]
    
        
        for i in range(n_strings):
            s1 = strs[i]
            s1Rep = find(s1)
            for j in range(i, n_strings):                
                s2 = strs[j]
                
                if s1Rep == find(s2):
                    continue
                
                if self.are_equaivalent(s1, s2):
                    union(s1, s2)
        
        
        unique_reps = set()
        
        
        for word in strs:
            unique_reps.add(find(word))
            
        return len(unique_reps)