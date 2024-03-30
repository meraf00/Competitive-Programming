class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):            
            task.append(i)
            
        tasks.sort()
        
        available = [(tasks[0][1], tasks[0][2])]
        
        time = tasks[0][0]
        
        i = 1
        
        ans = []
        
        while i < len(tasks):
            # get available
            while i < len(tasks) and tasks[i][0] <= time:                
                heappush(available, (tasks[i][1], tasks[i][2]))
                i += 1
                
            if not available:                               
                if i < len(tasks):
                    time = tasks[i][0]                
                continue
            
            # process            
            proc_time, task_idx = heappop(available)
            time += proc_time
            ans.append(task_idx)
        
        while available:
            ans.append(heappop(available)[1])
            
        return ans
            
            
            
        
        
        