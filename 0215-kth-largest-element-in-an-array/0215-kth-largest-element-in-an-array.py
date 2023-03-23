class Solution:
    def quicksort(self, start, end, array, k):
        if start >= end:
            return

        pivot = array[start]

        write_idx = start + 1

        for read_idx in range(start + 1, end + 1):
            if array[read_idx] <= pivot:
                array[read_idx], array[write_idx] = array[write_idx], array[read_idx]
                write_idx += 1

        array[write_idx - 1], array[start] = array[start], array[write_idx - 1]
                        
        if write_idx <= len(array) - k:
            self.quicksort(write_idx, end, array, k)
        
        else:   
            self.quicksort(start, write_idx - 2, array, k)
            
    
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quicksort(0, len(nums)-1, nums, k)
        
        return nums[-k]