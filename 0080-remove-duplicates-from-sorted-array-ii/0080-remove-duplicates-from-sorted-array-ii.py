class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        
        write = 0         
        
        count = 0
        
        last_read = None
        
        for read in range(length):                        
            if nums[read] == last_read:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[write] = nums[read]
                write += 1  
            
            last_read = nums[read]
        
        return write