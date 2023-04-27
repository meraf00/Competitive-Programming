class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        nums = list(set(nums))
        
        found = False        
        def quicksort(nums, start, end):
            nonlocal found
            
            
            if start >= end:
                found = True
                return
            
            
            pivot = nums[start]
            
            write_idx = start + 1
            
            for read_idx in range(start + 1, end + 1):
                if count[nums[read_idx]] <= count[pivot]:
                    nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
                    write_idx += 1
            
            
            nums[write_idx - 1], nums[start] = nums[start], nums[write_idx - 1]
            
            
            quicksort(nums, start, write_idx - 2)
            quicksort(nums, write_idx, end)
            
            return nums
        
        quicksort(nums, 0, len(nums) - 1)
                
        return nums[-k:]