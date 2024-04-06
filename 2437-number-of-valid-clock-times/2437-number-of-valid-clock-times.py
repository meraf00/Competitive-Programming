class Solution:
    def countTime(self, time: str) -> int:
        h = 1
        m = 1
        
        if time[0] == '?':            
            if time[1] == '?':
                h = 24
            elif int(time[1]) <= 3:
                h = 3
            else:
                h = 2               
        
        if time[1] == '?':
            if time[0] != '?':
                if int(time[0]) == 2:
                    h = 4
                else:
                    h = 10
        
        
        if time[3] == '?':
            if time[4] == '?':
                m = 60
            else:
                m = 6
            
            
        if time[4] == '?':
            if time[3] != '?':                
                m = 10
        
        
        return h * m
            
                