class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pref = [[-1] * n for _ in range(n)]
        
        
        for person in range(n):
            for j, friend in enumerate(preferences[person]):
                pref[person][friend] = j
        
        
        pair = {}
        
        for x, y in pairs:
            pair[x] = y
            pair[y] = x
        
        annoyed_friends = set()
        
        for x in range(n):
            y = pair[x]
            
            for u in range(n):                
                v = pair[u]
                
                if u == y or v == x or v == y:                    
                    continue
            
                if pref[x][u] < pref[x][y] and pref[u][x] < pref[u][v]:
                    annoyed_friends.add(x)                    
                
        return len(annoyed_friends)
                
                