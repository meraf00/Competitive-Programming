class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # contains elements in decreasing order
        # max_queue[0] - maximum element of current window
        max_queue = deque()
        
        # contains elements in increasing order
        # min_queue[0] - minimum element of current window
        min_queue = deque()
        
        max_length = 0
        left = 0
        for right, num in enumerate(nums):
            while min_queue and min_queue[-1] > num:
                min_queue.pop()
            
            min_queue.append(num)
            
            while max_queue and max_queue[-1] < num:
                max_queue.pop()
            
            max_queue.append(num)                        
            
            if max_queue[0] - min_queue[0] <= limit:
                max_length = max(max_length, right - left + 1)  
            else:
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                left += 1
        
        return max_length