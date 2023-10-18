class DSU:
    def __init__(self, n):
        self.reps = [i for i in range(n)]
        self.ranks = [1] * n
               
    def find(self, member):
        root = member
        while root != self.reps[root]:
            root = self.reps[root]


        while member != root:
            parent = self.reps[member]
            self.reps[member] = root
            member = parent

        return root

        
    def union(self, x, y):
        xRep = self.find(x)
        yRep = self.find(y)

        if xRep == yRep:                
            return

        if self.ranks[xRep] > self.ranks[yRep]:
            self.reps[yRep] = xRep
            self.ranks[xRep] += self.ranks[yRep]                                

        else:
            self.reps[xRep] = yRep
            self.ranks[yRep] += self.ranks[xRep]                

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # sort meetings by time
        meetings.append([-1, -1, float('inf')])
        
        meetings.sort(key = lambda x: x[-1])
        
        dsu = DSU(n)
        
        dsu.union(0, firstPerson)
                                
        left = 0
        
        for right in range(len(meetings)):             
            if meetings[right][2] != meetings[left][2]:                                
                people_at_time = set()                
                
                for i in range(left, right):
                    p1, p2, time = meetings[i]
                    
                    dsu.union(p1, p2)
                    people_at_time.add(p1)
                    people_at_time.add(p2)
                
                for p in people_at_time:
                    if dsu.find(p) != dsu.find(0):
                        dsu.reps[p] = p  
                    
                left = right
           
        ans = []
        
        rep = dsu.find(0)
        
        for person in range(n):
            if dsu.find(person) == rep:
                ans.append(person)
        
        return ans
        
            
                