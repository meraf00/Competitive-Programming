class Solution:
    def maximumTime(self, time: str) -> str:
        hour, minute = time.split(':')        
        
        max_hour = [hour[0], hour[1]]
        if hour[0] == '?':
            if hour[1] == '?':
                max_hour[0] = '2'
                max_hour[1] = '3'
            
            elif hour[1] <= '3':
                max_hour[0] = '2'                
            
            else:
                max_hour[0] = '1'                
        
        elif hour[1] == '?':
            if hour[0] < '2':                
                max_hour[1] = '9'
            
            else:                
                max_hour[1] = '3'
        
        max_min = [minute[0], minute[1]]
        if minute[0] == '?':
            max_min[0] = '5'
            
        if minute[1] == '?':
            max_min[1] = '9'
          
        return f"{''.join(max_hour)}:{''.join(max_min)}"