class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        def hash_(word):
            h = 0
            for char in word:
                i = ord(char) - ord('a')                
                h |= (1 << i)            
            return h
    
        def diff(word1, word2):
            return (hash_(word1) & hash_(word2)).bit_count()
    
        w = [hash_(word) for word in words]
        
        reps = {s:s for s in w}
        ranks = {s:1 for s in w}
        
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
            
            if ranks[xRep] < ranks[yRep]:
                reps[xRep] = yRep
                ranks[yRep] += ranks[xRep]
            
            else:
                reps[yRep] = xRep
                ranks[xRep] += ranks[yRep]
        
        
        counter = Counter(w)
        
        for word in w:
            for i in range(26):
                nbr = word ^ (1 << i)
                
                if nbr in counter:
                    union(word, nbr)
            
            for i in range(26):
                flag = (1 << i)
                
                if word & flag != 0:
                    swapped = word & (~flag)                                        
                    for j in range(i, 26):
                        flag = (1 << j)
                        
                        if swapped & flag == 0:
                            nbr = swapped ^ flag
                            
                            if nbr in counter:
                                union(word, nbr)
                        
        count = defaultdict(int)
        
        for word in w:
            rep = find(word)            
            count[rep] += 1
            
            
        groups = len(count)
        max_group = max(count.values())
        
        return [groups, max_group]
                    
                    
                