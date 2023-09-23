class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        reps = {i: i for i in nums}
        rank = {i: 1 for i in nums}
                
        def find(member):
            root = member
            while root != reps[root]:
                root = reps[root]
            
            parent = member
            while parent != root:
                temp = reps[parent]
                reps[parent] = root
                parent = temp
            
            return root
        
        
        def union(x, y):
            xRep = find(x)
            yRep = find(y)
            
            if xRep == yRep:
                return
            
            if rank[xRep] >= rank[yRep]:
                reps[yRep] = xRep
                rank[xRep] += rank[yRep]
            
            else:
                reps[xRep] = yRep
                rank[yRep] += rank[xRep]
            
                    
        for num in nums:
            if num - 1 in reps:
                union(num, num - 1)
        
        
        return max(rank.values())
                
        