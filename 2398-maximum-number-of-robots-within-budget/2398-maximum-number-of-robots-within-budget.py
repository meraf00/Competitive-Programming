class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        running_cost_prefix = [0]
        
        for num in runningCosts:
            running_cost_prefix.append(running_cost_prefix[-1] + num)                
        
        n = len(chargeTimes)
        
        queue = deque()
        
        left = 0                
        
        max_consecutive = 0
        
        right_moved = True
        
        right = 0
        
        while right < n:
            
            if right_moved:
                while queue and queue[-1] < chargeTimes[right]:
                    queue.pop()

                queue.append(chargeTimes[right])
            
            total_running_cost = running_cost_prefix[right + 1] - running_cost_prefix[left]
                        
            max_charge_time = queue[0]
                        
            k = right - left + 1
            
            cost = max_charge_time + k * total_running_cost
            
            if cost <= budget:                
                max_consecutive = max(max_consecutive, k)
                right_moved = True
                right += 1
            
            else:
                right_moved = False
                
                if queue and queue[0] == chargeTimes[left]:
                    queue.popleft()
                                
                left += 1
                
                if left > right:
                    right_moved = True
                    right = left
                        
        return max_consecutive