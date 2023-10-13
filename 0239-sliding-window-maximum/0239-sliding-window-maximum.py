class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        queue = deque()                    
        
        for right in range(k):
            while queue and queue[-1] < nums[right]:
                queue.pop()
            
            queue.append(nums[right])
        
        
        ans = [queue[0]]
                
        
        for right in range(k, n):
            if nums[right - k] == queue[0]:                
                queue.popleft()
                
            while queue and queue[-1] < nums[right]:
                queue.pop()
            
            queue.append(nums[right])              
                        
            ans.append(queue[0])        
        
        return ans