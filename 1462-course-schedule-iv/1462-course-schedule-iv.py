class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isPrereq = [[False] * numCourses for _ in range(numCourses)]                
        
        for a, b in prerequisites:
            isPrereq[a][b] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    isPrereq[i][j] = isPrereq[i][j] or (isPrereq[i][k] and isPrereq[k][j])
        
        ans = []
        
        for a, b in queries:
            ans.append(isPrereq[a][b])
            
        return ans
        
        
        