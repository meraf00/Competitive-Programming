class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {c : c for c in string.ascii_lowercase}
        
        rank = {c : 1 for c in string.ascii_lowercase}                
        
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
        
        
        for a, b in zip(s1, s2):
            union(a, b)
        
        
        # substitution table
        min_chars = {}
        
        for char in string.ascii_lowercase:
            charRep = find(char)
            
            if charRep in min_chars:
                min_chars[charRep] = min(min_chars[charRep], char)
            
            else:
                min_chars[charRep] = char
        
        
        answer = []
        
        for char in baseStr:
            charRep = find(char)
            answer.append(min_chars[charRep])
        
        return "".join(answer)
            