class Solution:
   
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:        
        unused = list(range(n))
        
        # (available_time, room_index)
        used = []
        
        meetings.sort()
        
        usage_count = defaultdict(int)
        
        max_usage = 0
        max_used_room = -1                
                
        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room_index = heappop(used)
                heappush(unused, room_index)
                                    
            if unused:                
                room_index = heappop(unused)                        
                heappush(used, (end, room_index))
            
            else:                
                available_time, room_index = heappop(used)
                
                duration = end - start
                heappush(used, (available_time + duration, room_index))
            
            usage_count[room_index] += 1            
            
            if usage_count[room_index] > max_usage:
                max_usage = usage_count[room_index]
                max_used_room = room_index
            
            if usage_count[room_index] == max_usage:
                max_usage = usage_count[room_index]
                max_used_room = min(max_used_room, room_index)
        
        
        return max_used_room
            

        
        
        
        

